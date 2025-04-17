import argparse
import subprocess
import os
from talk_openai import MyOpenAI  # For OpenAI interactions
from talk_ollama import Ollama  # For Ollama interactions
from iris_inference import run_inference  # Import the Iris inference function
from demo_productining_inference_script import generate_inference_script  # For script generation
from filesystem_explorer import explore_filesystem  # Filesystem exploration

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="CLI Tool for Deploy Wizard")

    # CLI options
    parser.add_argument('--model', type=str, choices=['openai', 'ollama', 'iris'], required=True, help='Select the AI model to use.')
    parser.add_argument('--api_key', type=str, help='API key for AI model (optional if set as environment variable).')  # Make api_key optional
    parser.add_argument('--task', type=str, required=True, choices=['chat', 'inference', 'script', 'explore_filesystem', 'deploy_terraform', 'deploy_docker'], help='Task to perform.')
    parser.add_argument('--input', type=str, required=True, help='Input for the selected task.')
    parser.add_argument('--terraform_config', type=str, help='Path to the Terraform configuration file (optional).')
    parser.add_argument('--dockerfile_path', type=str, help='Path to the Dockerfile (optional).')

    # Parse the arguments
    args = parser.parse_args()

    # Prompt for missing arguments if they are not passed
    if not args.model:
        args.model = input("Please enter the model (openai/ollama/iris): ")

    # Skip API key prompt for Ollama
    if args.model != 'ollama' and not args.api_key:
        args.api_key = input("Please enter your API key: ")

    if not args.terraform_config and args.task == 'deploy_terraform':
        args.terraform_config = input("Please provide the path to the Terraform configuration file (e.g., config.tfvars): ")
    if not args.dockerfile_path and args.task == 'deploy_docker':
        args.dockerfile_path = input("Please provide the path to the Dockerfile: ")

    # Use API key from environment if not passed via argument
    api_key = args.api_key if args.api_key else os.getenv("OPENAI_API_KEY")
    if not api_key and args.model != 'ollama':
        raise ValueError("API key is missing. Please provide it either through the command line or environment variable.")

    # Initialize the model
    model = None
    if args.model == 'openai':
        model = MyOpenAI()  # Initialize OpenAI model using the provided API key
    elif args.model == 'ollama':
        model = Ollama(model_name=args.input)  # Initialize Ollama model with dynamic choice
    elif args.model == 'iris':
        model = None  # Iris is handled separately, no model initialization needed

    # Execute the task based on the selected task
    if args.task == 'chat':
        print(f"Chatting with {args.model}...\nType 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Exiting chat.")
                break
            if args.model == 'ollama':
                response = model.invoke(user_input)  # Call Ollama's invoke method
            else:
                response = model.get_response(user_input)  # Assuming this method exists for OpenAI models
            print(f"Response: {response}")

    elif args.task == 'inference':
        print("Running inference...")
        if args.model == 'iris':
            # Parse features from the input (e.g., for Iris model)
            input_data = [float(x) for x in args.input.split(',')]
            result = run_inference(input_data)  # Perform inference using the Iris model
            print(f"Inference Result: {result}")
        else:
            print("Invalid model for inference.")

    elif args.task == 'script':
        print("Generating script...")
        generate_inference_script(args.input)  # Generate inference script based on input description

    elif args.task == 'explore_filesystem':
        print("Exploring filesystem...")
        explore_filesystem(args.input if args.input else None)  # Pass the directory if provided

    elif args.task == 'deploy_terraform':
        print("Deploying with Terraform...")
        if args.terraform_config:
            subprocess.run([
                "terraform", "apply", "-auto-approve", 
                "-var-file", args.terraform_config
            ], check=True)
            print("Terraform deployment complete.")
        else:
            print("Please provide the path to a Terraform configuration file.")

    elif args.task == 'deploy_docker':
        print("Deploying Docker container...")
        if args.dockerfile_path:
            subprocess.run([
                "docker", "build", "-t", "my_image", args.dockerfile_path
            ], check=True)
            print("Docker deployment complete.")
        else:
            print("Please provide the path to a Dockerfile.")

if __name__ == '__main__':
    main()
