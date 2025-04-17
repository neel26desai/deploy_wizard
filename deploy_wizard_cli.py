# import argparse
# import os
# from iris_inference import run_inference  # Import the Iris inference function
# from demo_productining_inference_script import generate_inference_script  # For script generation
# from talk_openai import MyOpenAI  # For OpenAI interactions
# from talk_ollama import Ollama  # For Ollama interactions
# from filesystem_explorer import explore_filesystem  # Filesystem exploration

# def main():
#     # Setup argument parser
#     parser = argparse.ArgumentParser(description="CLI Tool for Deploy Wizard")

#     # CLI options
#     parser.add_argument('--model', type=str, choices=['openai', 'ollama', 'iris'], required=True, help='Select the AI model to use.')
#     parser.add_argument('--api_key', type=str, help='API key for AI model (optional if set as environment variable).')  # Make api_key optional
#     parser.add_argument('--task', type=str, required=True, choices=['chat', 'inference', 'script', 'explore_filesystem'], help='Task to perform.')
#     parser.add_argument('--input', type=str, required=True, help='Input for the selected task.')

#     # Parse the arguments
#     args = parser.parse_args()

#     # Use API key from environment if not passed via argument
#     api_key = args.api_key if args.api_key else os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         raise ValueError("API key is missing. Please provide it either through the command line or environment variable.")

#     # Initialize the model
#     model = None
#     if args.model == 'openai':
#         model = MyOpenAI()  # Initialize OpenAI model using the provided API key
#     elif args.model == 'ollama':
#         model = Ollama(model_name=args.input)  # Initialize Ollama model with dynamic choice
#     elif args.model == 'iris':
#         model = None  # Iris is handled separately, no model initialization needed

#     # Execute the task based on the selected task
#     if args.task == 'chat':
#         print(f"Chatting with {args.model}...")
#         response = model.invoke(args.input)  # Use the input text to chat with OpenAI or Ollama
#         print(f"Response: {response}")

#     elif args.task == 'inference':
#         print("Running inference...")
#         if args.model == 'iris':
#             # Parse features from the input (e.g., for Iris model)
#             input_data = [float(x) for x in args.input.split(',')]
#             result = run_inference(input_data)  # Perform inference using the Iris model
#             print(f"Inference Result: {result}")
#         else:
#             print("Invalid model for inference.")

#     elif args.task == 'script':
#         print("Generating script...")
#         generate_inference_script(args.input)  # Generate inference script based on input description

#     # elif args.task == 'explore_filesystem':
#     #     print("Exploring filesystem...")
#     #     explore_filesystem()  # Explore files in the current directory

#     # Update in the CLI code where we handle the 'explore_filesystem' task
#     elif args.task == 'explore_filesystem':
#         print("Exploring filesystem...")
#         explore_filesystem(args.input if args.input else None)  # Pass the directory if provided


# if __name__ == '__main__':
#     main()

# import argparse
# import subprocess
# from talk_openai import MyOpenAI  # For OpenAI interactions
# from talk_ollama import Ollama  # For Ollama interactions
# from iris_inference import run_inference  # Import the Iris inference function
# from demo_productining_inference_script import generate_inference_script  # For script generation
# from filesystem_explorer import explore_filesystem  # Filesystem exploration

# def main():
#     # Setup argument parser
#     parser = argparse.ArgumentParser(description="CLI Tool for Deploy Wizard")

#     # CLI options
#     parser.add_argument('--model', type=str, choices=['openai', 'ollama', 'iris'], help='Select the AI model to use.')
#     parser.add_argument('--api_key', type=str, help='API key for AI model (optional if set as environment variable).')
#     parser.add_argument('--task', type=str, required=True, choices=['chat', 'inference', 'script', 'explore_filesystem', 'deploy_terraform', 'deploy_docker'], help='Task to perform.')
#     parser.add_argument('--input', type=str, required=True, help='Input for the selected task.')
#     parser.add_argument('--terraform_config', type=str, help='Path to the Terraform configuration file (optional).')
#     parser.add_argument('--dockerfile_path', type=str, help='Path to the Dockerfile (optional).')

#     # Parse the arguments
#     args = parser.parse_args()

#     # Prompt for missing arguments if they are not passed
#     if not args.model:
#         args.model = input("Please enter the model (openai/ollama/iris): ")

#     # Skip API key prompt for Ollama
#     if args.model != 'ollama' and not args.api_key:
#         args.api_key = input("Please enter your API key: ")

#     if not args.terraform_config and args.task == 'deploy_terraform':
#         args.terraform_config = input("Please provide the path to the Terraform config file: ")
#     if not args.dockerfile_path and args.task == 'deploy_docker':
#         args.dockerfile_path = input("Please provide the path to the Dockerfile: ")

#     # Use API key from environment if not passed via argument
#     if args.model != 'ollama' and not args.api_key:
#         raise ValueError("API key is missing. Please provide it either through the command line or environment variable.")

#     # Initialize the model
#     model = None
#     if args.model == 'openai':
#         model = MyOpenAI()  # Initialize OpenAI model using the provided API key
#     elif args.model == 'ollama':
#         model = Ollama(model_name=args.input)  # Initialize Ollama model with dynamic choice
#     elif args.model == 'iris':
#         model = None  # Iris is handled separately, no model initialization needed

#     # Execute the task based on the selected task
#     if args.task == 'chat':
#         print(f"Chatting with {args.model}...\nType 'exit' to quit.")
#         while True:
#             # Get user input
#             user_input = input("You: ")

#             # Exit loop if user types 'exit'
#             if user_input.lower() == 'exit':
#                 print("Exiting chat.")
#                 break

#             # Get response from the selected model
#             response = model.invoke(user_input)
#             print(f"Response: {response}")

#     elif args.task == 'inference':
#         print("Running inference...")
#         if args.model == 'iris':
#             # Parse features from the input (e.g., for Iris model)
#             input_data = [float(x) for x in args.input.split(',')]
#             result = run_inference(input_data)  # Perform inference using the Iris model
#             print(f"Inference Result: {result}")
#         else:
#             print("Invalid model for inference.")

#     elif args.task == 'script':
#         print("Generating script...")
#         generate_inference_script(args.input)  # Generate inference script based on input description

#     elif args.task == 'explore_filesystem':
#         print("Exploring filesystem...")
#         explore_filesystem(args.input if args.input else None)  # Pass the directory if provided

#     elif args.task == 'deploy_terraform':
#         print("Deploying with Terraform...")
#         if args.terraform_config:
#             # Run terraform apply command if a config path is provided
#             subprocess.run(["terraform", "apply", "-auto-approve", "-var-file", args.terraform_config], check=True)
#             print("Terraform deployment complete.")
#         else:
#             print("Please provide the path to a Terraform configuration file.")

#     elif args.task == 'deploy_docker':
#         print("Deploying Docker container...")
#         if args.dockerfile_path:
#             # Run docker build command if a Dockerfile path is provided
#             subprocess.run(["docker", "build", "-t", "my_image", args.dockerfile_path], check=True)
#             print("Docker deployment complete.")
#         else:
#             print("Please provide the path to a Dockerfile.")

# if __name__ == '__main__':
#     main()

# worksssssss for openai and ollama
# import argparse
# import subprocess
# from talk_openai import MyOpenAI  # For OpenAI interactions
# from talk_ollama import Ollama  # For Ollama interactions
# from iris_inference import run_inference  # Import the Iris inference function
# from demo_productining_inference_script import generate_inference_script  # For script generation
# from filesystem_explorer import explore_filesystem  # Filesystem exploration

# def main():
#     # Setup argument parser
#     parser = argparse.ArgumentParser(description="CLI Tool for Deploy Wizard")

#     # CLI options
#     parser.add_argument('--model', type=str, choices=['openai', 'ollama', 'iris'], help='Select the AI model to use.')
#     parser.add_argument('--api_key', type=str, help='API key for AI model (optional if set as environment variable).')
#     parser.add_argument('--task', type=str, required=True, choices=['chat', 'inference', 'script', 'explore_filesystem', 'deploy_terraform', 'deploy_docker'], help='Task to perform.')
#     parser.add_argument('--input', type=str, required=True, help='Input for the selected task.')
#     parser.add_argument('--terraform_config', type=str, help='Path to the Terraform configuration file (optional).')
#     parser.add_argument('--dockerfile_path', type=str, help='Path to the Dockerfile (optional).')

#     # Parse the arguments
#     args = parser.parse_args()

#     # Prompt for missing arguments if they are not passed
#     if not args.model:
#         args.model = input("Please enter the model (openai/ollama/iris): ")

#     # Skip API key prompt for Ollama
#     if args.model != 'ollama' and not args.api_key:
#         args.api_key = input("Please enter your API key: ")

#     if not args.terraform_config and args.task == 'deploy_terraform':
#         args.terraform_config = input("Please provide the path to the Terraform config file: ")
#     if not args.dockerfile_path and args.task == 'deploy_docker':
#         args.dockerfile_path = input("Please provide the path to the Dockerfile: ")

#     # Use API key from environment if not passed via argument
#     if args.model != 'ollama' and not args.api_key:
#         raise ValueError("API key is missing. Please provide it either through the command line or environment variable.")

#     # Initialize the model
#     model = None
#     if args.model == 'openai':
#         model = MyOpenAI()  # Initialize OpenAI model using the provided API key
#     elif args.model == 'ollama':
#         # Ollama model selection
#         model_name = args.input  # Use the model name from input for Ollama (e.g., gemma, gemma2, etc.)
#         model = Ollama(model_name=model_name)  # Initialize Ollama model with the dynamic choice
#     elif args.model == 'iris':
#         model = None  # Iris is handled separately, no model initialization needed

#     # Execute the task based on the selected task
#     if args.task == 'chat':
#         print(f"Chatting with {args.model}...\nType 'exit' to quit.")
#         while True:
#             # Get user input
#             user_input = input("You: ")

#             # Exit loop if user types 'exit'
#             if user_input.lower() == 'exit':
#                 print("Exiting chat.")
#                 break

#             # Get response from the selected model
#             if args.model == 'ollama':
#                 response = model.invoke(user_input)  # Call Ollama's invoke method
#             else:
#                 response = model.get_response(user_input)  # Assuming this method exists for OpenAI models
#             print(f"Response: {response}")

#     elif args.task == 'inference':
#         print("Running inference...")
#         if args.model == 'iris':
#             # Parse features from the input (e.g., for Iris model)
#             input_data = [float(x) for x in args.input.split(',')]
#             result = run_inference(input_data)  # Perform inference using the Iris model
#             print(f"Inference Result: {result}")
#         else:
#             print("Invalid model for inference.")

#     elif args.task == 'script':
#         print("Generating script...")
#         generate_inference_script(args.input)  # Generate inference script based on input description

#     elif args.task == 'explore_filesystem':
#         print("Exploring filesystem...")
#         explore_filesystem(args.input if args.input else None)  # Pass the directory if provided

#     elif args.task == 'deploy_terraform':
#         print("Deploying with Terraform...")
#         if args.terraform_config:
#             # Run terraform apply command if a config path is provided
#             subprocess.run(["terraform", "apply", "-auto-approve", "-var-file", args.terraform_config], check=True)
#             print("Terraform deployment complete.")
#         else:
#             print("Please provide the path to a Terraform configuration file.")

#     elif args.task == 'deploy_docker':
#         print("Deploying Docker container...")
#         if args.dockerfile_path:
#             # Run docker build command if a Dockerfile path is provided
#             subprocess.run(["docker", "build", "-t", "my_image", args.dockerfile_path], check=True)
#             print("Docker deployment complete.")
#         else:
#             print("Please provide the path to a Dockerfile.")

# if __name__ == '__main__':
#     main()

# import argparse
# import subprocess
# from talk_openai import MyOpenAI  # For OpenAI interactions
# from talk_ollama import Ollama  # For Ollama interactions
# from iris_inference import run_inference  # Import the Iris inference function
# from demo_productining_inference_script import generate_inference_script  # For script generation
# from filesystem_explorer import explore_filesystem  # Filesystem exploration

# def main():
#     # Setup argument parser
#     parser = argparse.ArgumentParser(description="CLI Tool for Deploy Wizard")

#     # CLI options
#     parser.add_argument('--model', type=str, choices=['openai', 'ollama', 'iris'], help='Select the AI model to use.')
#     parser.add_argument('--api_key', type=str, help='API key for AI model (optional if set as environment variable).')
#     parser.add_argument('--task', type=str, required=True, choices=['chat', 'inference', 'script', 'explore_filesystem', 'deploy_terraform', 'deploy_docker'], help='Task to perform.')
#     parser.add_argument('--input', type=str, required=True, help='Input for the selected task.')
#     parser.add_argument('--terraform_config', type=str, help='Path to the Terraform configuration file (optional).')
#     parser.add_argument('--dockerfile_path', type=str, help='Path to the Dockerfile (optional).')

#     # Parse the arguments
#     args = parser.parse_args()

#     # Prompt for missing arguments if they are not passed
#     if not args.model:
#         args.model = input("Please enter the model (openai/ollama/iris): ")

#     # Skip API key prompt for Ollama
#     if args.model != 'ollama' and not args.api_key:
#         args.api_key = input("Please enter your API key: ")

#     if not args.terraform_config and args.task == 'deploy_terraform':
#         args.terraform_config = input("Please provide the path to the Terraform config file: ")
#     if not args.dockerfile_path and args.task == 'deploy_docker':
#         args.dockerfile_path = input("Please provide the path to the Dockerfile: ")

#     # Use API key from environment if not passed via argument
#     if args.model != 'ollama' and not args.api_key:
#         raise ValueError("API key is missing. Please provide it either through the command line or environment variable.")

#     # Initialize the model
#     model = None
#     if args.model == 'openai':
#         model = MyOpenAI()  # Initialize OpenAI model using the provided API key
#     elif args.model == 'ollama':
#         # Ollama model selection
#         model_name = args.input  # Use the model name from input for Ollama (e.g., gemma, gemma2, etc.)
#         model = Ollama(model_name=model_name)  # Initialize Ollama model with the dynamic choice
#     elif args.model == 'iris':
#         model = None  # Iris is handled separately, no model initialization needed

#     # Execute the task based on the selected task
#     if args.task == 'chat':
#         print(f"Chatting with {args.model}...\nType 'exit' to quit.")
#         while True:
#             # Get user input
#             user_input = input("You: ")

#             # Exit loop if user types 'exit'
#             if user_input.lower() == 'exit':
#                 print("Exiting chat.")
#                 break

#             # Get response from the selected model
#             if args.model == 'ollama':
#                 response = model.invoke(user_input)  # Call Ollama's invoke method
#             else:
#                 response = model.get_response(user_input)  # Assuming this method exists for OpenAI models
#             print(f"Response: {response}")

#     elif args.task == 'inference':
#         print("Running inference...")
#         if args.model == 'iris':
#             # Parse features from the input (e.g., for Iris model)
#             input_data = [float(x) for x in args.input.split(',')]
#             result = run_inference(input_data)  # Perform inference using the Iris model
#             print(f"Inference Result: {result}")
#         else:
#             print("Invalid model for inference.")

#     elif args.task == 'script':
#         print("Generating script...")
#         generate_inference_script(args.input)  # Generate inference script based on input description

#     elif args.task == 'explore_filesystem':
#         print("Exploring filesystem...")
#         explore_filesystem(args.input if args.input else None)  # Pass the directory if provided

#     elif args.task == 'deploy_terraform':
#         print("Deploying with Terraform...")
#         if args.terraform_config:
#             # Run terraform apply command if a config path is provided
#             subprocess.run(["terraform", "apply", "-auto-approve", "-var-file", args.terraform_config], check=True)
#             print("Terraform deployment complete.")
#         else:
#             print("Please provide the path to a Terraform configuration file.")

#     elif args.task == 'deploy_docker':
#         print("Deploying Docker container...")
#         if args.dockerfile_path:
#             # Run docker build command if a Dockerfile path is provided
#             subprocess.run(["docker", "build", "-t", "my_image", args.dockerfile_path], check=True)
#             print("Docker deployment complete.")
#         else:
#             print("Please provide the path to a Dockerfile.")

# if __name__ == '__main__':
#     main()

import argparse
import subprocess
from talk_openai import MyOpenAI  # For OpenAI interactions
from talk_ollama import Ollama  # For Ollama interactions
from iris_inference import run_inference  # Import the Iris inference function
from demo_productining_inference_script import generate_inference_script  # For script generation
from filesystem_explorer import explore_filesystem  # Filesystem exploration

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="CLI Tool for Deploy Wizard")

    # CLI options
    parser.add_argument('--model', type=str, choices=['openai', 'ollama', 'iris'], help='Select the AI model to use.')
    parser.add_argument('--api_key', type=str, help='API key for AI model (optional if set as environment variable).')
    parser.add_argument('--task', type=str, required=True, choices=['chat', 'inference', 'script', 'explore_filesystem', 'deploy_terraform', 'deploy_docker'], help='Task to perform.')
    parser.add_argument('--input', type=str, required=True, help='Input for the selected task.')
    parser.add_argument('--terraform_config', type=str, help='Path to the Terraform configuration file (optional).')
    parser.add_argument('--dockerfile_path', type=str, help='Path to the Dockerfile (optional).')

    # Parse the arguments
    args = parser.parse_args()

    # Only ask for the model if it's not a Terraform or Docker task
    if args.task not in ['deploy_terraform', 'deploy_docker'] and not args.model:
        args.model = input("Please enter the model (openai/ollama/iris): ")

    # Skip the API key prompt if the task is Terraform or Docker
    if args.task not in ['deploy_terraform', 'deploy_docker'] and not args.api_key:
        args.api_key = input("Please enter your API key: ")

    if args.task == 'deploy_terraform' and not args.terraform_config:
        args.terraform_config = input("Please provide the path to the Terraform configuration file (e.g., config.tfvars): ")

    if args.task == 'deploy_docker' and not args.dockerfile_path:
        args.dockerfile_path = input("Please provide the path to the Dockerfile: ")

    # Use API key from environment if not passed via argument (skip for Terraform and Docker)
    if args.model not in ['ollama', 'openai'] and not args.api_key and args.task not in ['deploy_terraform', 'deploy_docker']:
        raise ValueError("API key is missing. Please provide it either through the command line or environment variable.")

    # Initialize the model
    model = None
    if args.model == 'openai':
        model = MyOpenAI()  # Initialize OpenAI model using the provided API key
    elif args.model == 'ollama':
        model_name = args.input  # Use the model name from input for Ollama (e.g., gemma, gemma2, etc.)
        model = Ollama(model_name=model_name)  # Initialize Ollama model with dynamic choice
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
            input_data = [float(x) for x in args.input.split(',')]
            result = run_inference(input_data)
            print(f"Inference Result: {result}")
        else:
            print("Invalid model for inference.")

    elif args.task == 'script':
        print("Generating script...")
        generate_inference_script(args.input)  # Generate inference script based on input description

    elif args.task == 'explore_filesystem':
        print("Exploring filesystem...")
        explore_filesystem(args.input if args.input else None)

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
