import argparse
import subprocess
import os
import json
from talk_openai import MyOpenAI
from talk_ollama import Ollama
from iris_inference import run_inference
from filesystem_explorer import explore_filesystem

MODEL_NAME = "gpt-4o-mini"

def validate_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found. Please provide a valid path.")
    if not file_path.endswith('.py'):
        raise ValueError("Unsupported file format. Only Python (.py) files are allowed.")
    return True

def generate_inference_script(file_path, api_key):
    inference_script_generator_llm = MyOpenAI(model=MODEL_NAME, api_key=api_key)
    if validate_file(file_path):
        print(f"File {file_path} is valid.")
        result = inference_script_generator_llm.invoke(f"Generate an inference script from the file {file_path}")
        print(result)

def get_azure_vm_ip(vm_name: str, resource_group: str) -> str:
    try:
        result = subprocess.run(
            [
                "az", "vm", "list-ip-addresses",
                "--name", vm_name,
                "--resource-group", resource_group,
                "--output", "json"
            ],
            capture_output=True, text=True, check=True
        )
        ip_info = json.loads(result.stdout)
        return ip_info[0]["virtualMachine"]["network"]["publicIpAddresses"][0]["ipAddress"]
    except Exception as e:
        return f"⚠️ Unable to fetch real Azure IP: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Unified Multi-Cloud Deploy CLI")

    parser.add_argument('--cloud', choices=['aws', 'azure'], help="Cloud platform to deploy to.")
    parser.add_argument('--model', choices=['openai', 'ollama', 'iris'], help="AI model to use.")
    parser.add_argument('--task', choices=[
        'chat', 'inference', 'script', 'explore_filesystem',
        'deploy_terraform', 'deploy_docker', 'generate_infra'
    ], required=True)
    parser.add_argument('--input', help="Input text, file, or data depending on the task.")
    parser.add_argument('--api_key', help="API key for OpenAI.")
    parser.add_argument('--terraform_config', help="Path to the Terraform config file.")
    parser.add_argument('--dockerfile_path', help="Path to Dockerfile folder.")
    parser.add_argument('--image_name', help="Docker image name to use.")
    parser.add_argument('--container_name', help="Name for the Docker container.")
    parser.add_argument('--model_port', help="Port the model should expose.")
    parser.add_argument('--public_ip_type', choices=['static', 'dynamic'], default='static',
                    help="Choose type of public IP (static or dynamic). Defaults to static.")


    args = parser.parse_args()

    if not args.cloud and args.task != 'generate_infra':
        args.cloud = input("Which cloud do you want to deploy to? (aws/azure): ").strip().lower()
    if not args.model:
        args.model = input("Select model (openai/ollama/iris): ").strip().lower()
    if args.model != 'ollama' and not args.api_key:
        args.api_key = input("Enter your OpenAI API key: ")
    if not args.input and args.task != 'generate_infra':
        args.input = input("Enter input (file path or data): ")

    if args.task == 'deploy_docker':
        if not args.image_name:
            args.image_name = input("Enter Docker image name: ")
        if not args.container_name:
            args.container_name = input("Enter container name: ")
        if not args.model_port:
            args.model_port = input("Enter exposed port: ")

    if args.task == 'deploy_terraform':
        if not args.terraform_config:
            args.terraform_config = input("Enter path to Terraform config (e.g. terraform.tfvars): ")
        tf_folder = f"{args.cloud}_terraform_files"
        if not os.path.exists(tf_folder):
            raise FileNotFoundError(f"Terraform folder '{tf_folder}' not found.")
        os.chdir(tf_folder)

    model = None
    if args.model == 'openai':
        model = MyOpenAI(model=MODEL_NAME, api_key=args.api_key)
    elif args.model == 'ollama':
        model = Ollama(model_name=args.input)

    if args.task == 'chat':
        print("Chatting (type 'exit' to quit):")
        while True:
            prompt = input("You: ")
            if prompt.lower() == 'exit': break
            if args.model == 'ollama':
                print("Response:", model.invoke(prompt))
            else:
                print("Response:", model.get_response(prompt))

    elif args.task == 'inference':
        if args.model == 'iris':
            features = [float(x) for x in args.input.split(',')]
            result = run_inference(features)
            print("Inference Result:", result)
        else:
            print("Inference only supported for 'iris' model.")

    elif args.task == 'script':
        print("Generating inference script...")
        generate_inference_script(args.input, args.api_key)

    elif args.task == 'explore_filesystem':
        explore_filesystem(args.input)

    elif args.task == 'deploy_terraform':
        subprocess.run([
            "terraform", "apply", "-auto-approve",
            "-var-file", args.terraform_config
        ], check=True)
        print("✅ Terraform deployment complete.")

        if args.cloud == "azure":
            print("\n🔍 Fetching actual public IP from Azure CLI...")
            real_ip = get_azure_vm_ip("azure-vm", "deploy-wizard-rg")
            port = args.model_port or "8000"
            print(f"\n✅ Live Azure VM IP: {real_ip}")
            print(f"🌐 Access your app at: http://{real_ip}:{port}/docs")
            print(f"🔐 SSH using: ssh azureuser@{real_ip}")

    elif args.task == 'generate_infra':
        cloud_choice = input("☁️ Which cloud platform are you targeting? (aws/azure): ").strip().lower()

        print("\n🧠 Describe the cloud infrastructure you want to deploy using Terraform.")
        print("💬 Include cloud platform, OS, Docker, and ports to expose.")
        print("💡 Example (AWS): 'Create an AWS EC2 with Docker. Run image mansiiv/iris_model_inference:latest on port 8000 and allow SSH.'")
        print("💡 Example (Azure): 'Deploy an Azure VM with Docker. Run image mansiiv/iris_model_inference:latest on port 8000.'")

        user_description = input("\n📝 What would you like to deploy? ").strip()

        if "port" not in user_description.lower():
            default_port = input("🔧 No port mentioned. What port should be exposed? [default: 8000]: ").strip() or "8000"
            while not default_port.isdigit():
                default_port = input("⚠️ Invalid input. Please enter a numeric port (e.g., 8000): ").strip()
            user_description += f". Also expose port {default_port} and allow SSH (port 22)."

        provider_hint = ""

        if "aws" in cloud_choice:
            region = input("🌍 Which AWS region? (default: us-east-1): ").strip() or "us-east-1"
            try:
                result = subprocess.run([
                    "aws", "ec2", "describe-images",
                    "--region", region,
                    "--owners", "amazon",
                    "--filters", "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2",
                    "Name=state,Values=available",
                    "--query", "Images[*].[ImageId,CreationDate]",
                    "--output", "text"
                ], capture_output=True, text=True, check=True)

                ami_id = sorted(
                    [line.split()[0] for line in result.stdout.strip().split('\n')],
                    reverse=True
                )[0]

                user_description += f" Use AMI ID {ami_id} in region {region}."
                provider_hint = (
                    "\nUse the AWS provider with aws_instance, aws_security_group, and user_data. "
                    "Install Docker and run a container on port 8000. Ensure port 22 and 8000 are open."
                )
            except Exception as e:
                print(f"⚠️ Failed to fetch AMI ID. Error: {e}")
                print("You may need to configure AWS CLI or use a hardcoded AMI.")

        elif "azure" in cloud_choice:
            print("🔐 Azure requires a subscription ID in the provider block.")
            print("💡 You can find your subscription ID by running this in your terminal:")
            print("   az account show --query id --output tsv")
            print("💡 Or go to Azure Portal → Subscriptions → Copy the Subscription ID.\n")

            subscription_id = input("📋 Paste your Azure subscription ID here: ").strip()
            
            # Determine public IP type (Static or Dynamic)
            ip_allocation = "Static" if args.public_ip_type == "static" else "Dynamic"
            ip_sku = "Standard" if args.public_ip_type == "static" else "Basic"

            provider_hint = (
                f"\nUse the azurerm provider with azurerm_linux_virtual_machine. "
                f"Set subscription_id = \"{subscription_id}\" in the provider block. "
                "Inside `os_disk`, include 'caching = \"ReadWrite\"' and 'storage_account_type = \"Standard_LRS\"'. "
                "Use `admin_ssh_key` with username = \"azureuser\" and public_key = file(\"~/.ssh/id_rsa.pub\"). "
                f"Use `azurerm_public_ip` with sku = \"{ip_sku}\" and allocation_method = \"{ip_allocation}\". "
                "Attach `public_ip_address_id` in the NIC `ip_configuration` block. "
                "Use `azurerm_network_interface_security_group_association` to connect the NIC to the NSG. "
                "Define NSG rules using `azurerm_network_security_rule`, with completely unique names and priorities. "
                "For example: use priority = 1005 for SSH and 1006 for HTTP. "
                "Use a `null_resource` with `remote-exec` to install Docker and run image mansiiv/iris_model_inference:latest."
    )


        print("\n📡 Sending prompt to OpenAI...")
        full_prompt = (
            "You are a Terraform expert. Generate only valid HCL Terraform code. "
            "Do NOT include markdown syntax (like ```), comments, or explanations. "
            "Return only the raw code for a .tf file.\n\n"
            f"{user_description}{provider_hint}"
        )

        tf_code = MyOpenAI(model=MODEL_NAME, api_key=args.api_key).invoke(full_prompt)

        os.makedirs("generated_tf", exist_ok=True)
        with open("generated_tf/main.tf", "w") as f:
            f.write(tf_code)

        print("✅ Terraform code saved to generated_tf/main.tf")
        print("📄 Preview:\n" + "-" * 60 + "\n" + tf_code[:600] + "\n" + "-" * 60)

        os.chdir("generated_tf")
        subprocess.run(["terraform", "init"], check=True)
        subprocess.run(["terraform", "apply", "-auto-approve"], check=True)
        print("\n🚀 Terraform apply complete. Check your cloud dashboard.")

if __name__ == '__main__':
    main()
