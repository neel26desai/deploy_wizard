import os
from talk_openai import MyOpenAI  # Import your MyOpenAI class to use OpenAI

# Define model name
MODEL_NAME = "gpt-4o-mini"

# Create an instance of the model (OpenAI or Ollama)
inference_script_generator_llm = MyOpenAI(model=MODEL_NAME)

def validate_file(file_path):
    """Validate if the file exists and is a Python script."""
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found. Please provide a valid path.")
    
    if not file_path.endswith('.py'):
        raise ValueError("Unsupported file format. Only Python (.py) files are allowed.")
    
    return True

def generate_inference_script(file_path):
    """Generate inference script based on the provided file path."""
    if validate_file(file_path):
        print(f"File {file_path} is valid.")
        # Inference logic based on the Python file can be added here
        result = inference_script_generator_llm.invoke(f"Generate an inference script from the file {file_path}")
        print(result)

def main(file_path):
    """Main function to execute the inference task."""
    generate_inference_script(file_path)

if __name__ == "__main__":
    # Example: replace this with actual file path or modify to get from CLI
    file_path = "path_to_your_python_file.py"  # You will pass this from the CLI
    main(file_path)
