import argparse
import os
from iris_inference import run_inference  # Import the Iris inference function
from demo_productining_inference_script import generate_inference_script  # For script generation
from talk_openai import MyOpenAI  # For OpenAI interactions
from talk_ollama import Ollama  # For Ollama interactions
from filesystem_explorer import explore_filesystem  # Filesystem exploration

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="CLI Tool for Deploy Wizard")

    # CLI options
    parser.add_argument('--model', type=str, choices=['openai', 'ollama', 'iris'], required=True, help='Select the AI model to use.')
    parser.add_argument('--api_key', type=str, help='API key for AI model (optional if set as environment variable).')  # Make api_key optional
    parser.add_argument('--task', type=str, required=True, choices=['chat', 'inference', 'script', 'explore_filesystem'], help='Task to perform.')
    parser.add_argument('--input', type=str, required=True, help='Input for the selected task.')

    # Parse the arguments
    args = parser.parse_args()

    # Use API key from environment if not passed via argument
    api_key = args.api_key if args.api_key else os.getenv("OPENAI_API_KEY")
    if not api_key:
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
        print(f"Chatting with {args.model}...")
        response = model.invoke(args.input)  # Use the input text to chat with OpenAI or Ollama
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

    # elif args.task == 'explore_filesystem':
    #     print("Exploring filesystem...")
    #     explore_filesystem()  # Explore files in the current directory

    # Update in the CLI code where we handle the 'explore_filesystem' task
    elif args.task == 'explore_filesystem':
        print("Exploring filesystem...")
        explore_filesystem(args.input if args.input else None)  # Pass the directory if provided


if __name__ == '__main__':
    main()
