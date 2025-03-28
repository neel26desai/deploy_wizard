import os

def explore_filesystem(directory=None):
    """Explores filesystem in the current or specified directory."""
    # Use current directory if no directory is passed
    if directory is None:
        directory = os.getcwd()

    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    print(f"Exploring directory: {directory}")

    # List files in the specified directory
    files = os.listdir(directory)
    if files:
        print("Files in the directory:")
        for file in files:
            print(f"- {file}")
    else:
        print("No files found in the directory.")
