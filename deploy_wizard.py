# import argparse
# import subprocess
# import os
# from talk_openai import MyOpenAI
# from talk_ollama import Ollama
# from iris_inference import run_inference
# from filesystem_explorer import explore_filesystem

# MODEL_NAME = "gpt-4o-mini"

# def validate_file(file_path):
#     if not os.path.exists(file_path):
#         raise FileNotFoundError("File not found. Please provide a valid path.")
#     if not file_path.endswith('.py'):
#         raise ValueError("Unsupported file format. Only Python (.py) files are allowed.")
#     return True

# def generate_inference_script(file_path, api_key):
#     inference_script_generator_llm = MyOpenAI(model=MODEL_NAME, api_key=api_key)
#     if validate_file(file_path):
#         print(f"File {file_path} is valid.")
#         result = inference_script_generator_llm.invoke(f"Generate an inference script from the file {file_path}")
#         print(result)

# import subprocess
# import json

# def get_azure_vm_ip(vm_name: str, resource_group: str) -> str:
#     try:
#         result = subprocess.run(
#             [
#                 "az", "vm", "list-ip-addresses",
#                 "--name", vm_name,
#                 "--resource-group", resource_group,
#                 "--output", "json"
#             ],
#             capture_output=True, text=True, check=True
#         )
#         ip_info = json.loads(result.stdout)
#         return ip_info[0]["virtualMachine"]["network"]["publicIpAddresses"][0]["ipAddress"]
#     except Exception as e:
#         return f"⚠️ Unable to fetch real Azure IP: {str(e)}"


# def main():
#     parser = argparse.ArgumentParser(description="Unified Multi-Cloud Deploy CLI")

#     parser.add_argument('--cloud', choices=['aws', 'azure'], help="Cloud platform to deploy to.")
#     parser.add_argument('--model', choices=['openai', 'ollama', 'iris'], help="AI model to use.")
#     parser.add_argument('--task', choices=['chat', 'inference', 'script', 'explore_filesystem', 'deploy_terraform', 'deploy_docker'], required=True)
#     parser.add_argument('--input', help="Input text, file, or data depending on the task.")
#     parser.add_argument('--api_key', help="API key for OpenAI.")
#     parser.add_argument('--terraform_config', help="Path to the Terraform config file.")
#     parser.add_argument('--dockerfile_path', help="Path to Dockerfile folder.")
#     parser.add_argument('--image_name', help="Docker image name to use.")
#     parser.add_argument('--container_name', help="Name for the Docker container.")
#     parser.add_argument('--model_port', help="Port the model should expose.")

#     args = parser.parse_args()

#     # Interactive prompts for missing fields
#     if not args.cloud:
#         args.cloud = input("Which cloud do you want to deploy to? (aws/azure): ").strip().lower()
#     if not args.model:
#         args.model = input("Select model (openai/ollama/iris): ").strip().lower()
#     if args.model != 'ollama' and not args.api_key:
#         args.api_key = input("Enter your OpenAI API key: ")
#     if not args.input:
#         args.input = input("Enter input (file path or data): ")

#     if args.task == 'deploy_docker':
#         if not args.image_name:
#             args.image_name = input("Enter Docker image name: ")
#         if not args.container_name:
#             args.container_name = input("Enter container name: ")
#         if not args.model_port:
#             args.model_port = input("Enter exposed port: ")

#     if args.task == 'deploy_terraform':
#         if not args.terraform_config:
#             args.terraform_config = input("Enter path to Terraform config (e.g. terraform.tfvars): ")
#         tf_folder = f"{args.cloud}_terraform_files"
#         if not os.path.exists(tf_folder):
#             raise FileNotFoundError(f"Terraform folder '{tf_folder}' not found.")
#         os.chdir(tf_folder)

#     model = None
#     if args.model == 'openai':
#         model = MyOpenAI(model="gpt-4o-mini", api_key=args.api_key)
#     elif args.model == 'ollama':
#         model = Ollama(model_name=args.input)

#     if args.task == 'chat':
#         print("Chatting (type 'exit' to quit):")
#         while True:
#             prompt = input("You: ")
#             if prompt.lower() == 'exit': break
#             if args.model == 'ollama':
#                 print("Response:", model.invoke(prompt))
#             else:
#                 print("Response:", model.get_response(prompt))

#     elif args.task == 'inference':
#         if args.model == 'iris':
#             features = [float(x) for x in args.input.split(',')]
#             result = run_inference(features)
#             print("Inference Result:", result)
#         else:
#             print("Inference only supported for 'iris' model.")

#     elif args.task == 'script':
#         print("Generating inference script...")
#         generate_inference_script(args.input, args.api_key)

#     elif args.task == 'explore_filesystem':
#         explore_filesystem(args.input)

#     elif args.task == 'deploy_terraform':
#         subprocess.run([
#             "terraform", "apply", "-auto-approve",
#             "-var-file", args.terraform_config
#         ], check=True)
#         print("Terraform deployment complete.")

#     elif args.task == 'deploy_docker':
#         subprocess.run([
#             "docker", "run", "-d",
#             "-p", f"{args.model_port}:{args.model_port}",
#             "--name", args.container_name,
#             args.image_name
#         ], check=True)
#         print("Docker container deployed.")

# if __name__ == '__main__':
#     main()



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
    parser.add_argument('--task', choices=['chat', 'inference', 'script', 'explore_filesystem', 'deploy_terraform', 'deploy_docker'], required=True)
    parser.add_argument('--input', help="Input text, file, or data depending on the task.")
    parser.add_argument('--api_key', help="API key for OpenAI.")
    parser.add_argument('--terraform_config', help="Path to the Terraform config file.")
    parser.add_argument('--dockerfile_path', help="Path to Dockerfile folder.")
    parser.add_argument('--image_name', help="Docker image name to use.")
    parser.add_argument('--container_name', help="Name for the Docker container.")
    parser.add_argument('--model_port', help="Port the model should expose.")

    args = parser.parse_args()

    if not args.cloud:
        args.cloud = input("Which cloud do you want to deploy to? (aws/azure): ").strip().lower()
    if not args.model:
        args.model = input("Select model (openai/ollama/iris): ").strip().lower()
    if args.model != 'ollama' and not args.api_key:
        args.api_key = input("Enter your OpenAI API key: ")
    if not args.input:
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

        # Show actual public IP if deploying to Azure
        if args.cloud == "azure":
            print("\n🔍 Fetching actual public IP from Azure CLI...")
            real_ip = get_azure_vm_ip("azure-vm", "deploy-wizard-rg")
            port = args.model_port or "8000"
            print(f"\n✅ Live Azure VM IP: {real_ip}")
            print(f"🌐 Access your app at: http://{real_ip}:{port}/docs")
            print(f"🔐 SSH using: ssh azureuser@{real_ip}")

    elif args.task == 'deploy_docker':
        subprocess.run([
            "docker", "run", "-d",
            "-p", f"{args.model_port}:{args.model_port}",
            "--name", args.container_name,
            args.image_name
        ], check=True)
        print("Docker container deployed.")

if __name__ == '__main__':
    main()
