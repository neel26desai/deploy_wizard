# Integrated Features:
Chat (OpenAI & Ollama): We integrated the ability to chat with two models, OpenAI and Ollama.

Inference: We integrated the Iris model to perform inference based on input values.

Script Generation: A dynamic script generation feature was added using OpenAI for creating inference scripts from a given Python file.

Filesystem Exploration: Added functionality to explore the filesystem by creating and manipulating files in a temporary directory.

---------------
Model Selection: The code was modified to dynamically select between models like openai, ollama, and iris based on user input.

New Tasks: Added new tasks like inference, script generation, and explore_filesystem to the CLI interface.

Model Interaction: Updated the code to handle both OpenAI and Ollama models, and added a dynamic handling mechanism for Iris inference.

CLI Argument Parsing: Improved parsing to accept model and task arguments, making it easy to switch between tasks and models.
----------------

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/deploy-wizard.git
    cd deploy-wizard
    ```

2. Set up the virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For macOS/Linux
    .venv\Scripts\activate     # For Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```


## Task Usage

### 1. **Chat with a Model**

To chat with the selected model (OpenAI, Ollama, Iris), run the following command:

#### For OpenAI:
```bash
python deploy_wizard_cli.py --model openai --task chat --input "What is the capital of France?"
```
For Ollama:

```bash
python deploy_wizard_cli.py --model ollama --task chat --input "What is the capital of France?"
```
2. Run Inference

Run inference for the Iris model with the following command:
```bash
python deploy_wizard_cli.py --model iris --task inference --input "5.1,3.5,1.4,0.2"
```
3. Generate Inference Script
To generate an inference script based on the provided Python file, use the following command:

```bash
python deploy_wizard_cli.py --model openai --task script --input "path_to_your_python_file.py"
```
4. Explore Filesystem
You can explore the filesystem within a temporary directory by using the following command:

```bash
python deploy_wizard_cli.py --model openai --task explore_filesystem --input "path_to_explore"
```
5. Example Command
For OpenAI chat task:

```bash
python deploy_wizard_cli.py --model openai --task chat --input "Hello, how are you?"
```


## Notes

### 1. **Dynamic Model and Task Handling**
The CLI tool has been designed to support dynamic model and task handling. Users can now seamlessly interact with different models (`openai`, `ollama`, `iris`) and perform various tasks (chat, inference, script generation, filesystem exploration) by specifying the model and task in the command. This makes the system flexible and extensible for different use cases.

### 2. **Task-Driven Architecture**
The CLI tool dynamically adjusts the behavior based on the task selected:
- **Chat**: Initiates a conversation with the selected model (OpenAI, Ollama, Iris) based on user input.
- **Inference**: Allows running inference on the Iris model, with inputs formatted as comma-separated values (e.g., "5.1,3.5,1.4,0.2").
- **Script Generation**: Generates Python inference scripts based on a given Python file. This task utilizes OpenAI for creating script templates.
- **Filesystem Exploration**: Explores the filesystem within a temporary directory, demonstrating file creation and reading.

### 3. **Environment Setup**
For the system to work correctly, it is important to set up the necessary environment variables or provide API keys as required by the models (e.g., OpenAI API Key). The API key can be set in the environment or passed as an argument in the CLI.

### 4. **CLI Argument Structure**
The following arguments are supported by the CLI:
- `--model`: Select the AI model to use (choices: `openai`, `ollama`, `iris`).
- `--task`: Specify the task to perform (choices: `chat`, `inference`, `script`, `explore_filesystem`).
- `--input`: The input for the selected task. This can be a string for chat tasks or comma-separated values for inference tasks.

### 5. **Model-Specific Notes**
- **OpenAI**: To chat with OpenAI models, ensure that the OpenAI API key is correctly set in the environment or passed via the CLI.
- **Ollama**: Ollama requires the model to be pulled before use. Ensure that the correct model is pulled using the `ollama pull` command.
- **Iris**: The Iris model is used for classification tasks. Ensure that the input data is numeric and follows the correct format for inference.

### 6. **Additional Features**
- **Dynamic Script Generation**: The script generation task utilizes OpenAI to automatically generate inference scripts from a Python file, enhancing the workflow for deploying AI models.
- **Filesystem Exploration**: This task is designed to demonstrate filesystem interactions in a temporary environment. It helps explore directories, create files, and read them dynamically.

### 7. **Flexibility and Extensibility**
This project has been structured to allow easy addition of new models and tasks. You can extend the functionality by:
- Adding new models and connecting them to the system.
- Adding new tasks to perform different operations based on user input.

### 8. **Error Handling**
Proper error handling has been implemented for each task:
- If a model or task is not found, an appropriate error message will be displayed.
- For invalid inputs (e.g., incorrect format or missing files), informative error messages are shown to guide the user.




