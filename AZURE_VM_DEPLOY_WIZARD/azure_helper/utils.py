import os
def read_openai_key(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except Exception as e:
        return str(e)

def file_reader(input_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError("File not found. Please provide a valid path.")
    try:
        with open(input_file, 'r') as file:
            return file.read()
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")

def get_file_path():
    """Prompt the user for the training Python file path."""
    file_path = input("Enter the path to the training Python file: ").strip()
    return file_path

def write_to_file(file_path, content):
    """Write the content to the specified file."""
    with open(file_path, 'w') as file:
        file.write(content)