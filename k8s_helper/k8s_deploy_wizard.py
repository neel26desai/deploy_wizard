from langchain.chat_models import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType
import os
import subprocess
from pydantic import BaseModel

class SaveFileInput(BaseModel):
    file_path: str
    content: str

@tool(args_schema=SaveFileInput)
def save_file_tool(file_path: str, content: str) -> str:
    """Save content to a file at the given path."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(content)
    return f"Saved to {file_path}"

class DeployKubernetes:
    def __init__(self, small_model="gpt-4o-mini", large_model="gpt-4o", actor_critic_iterations=1):
        self.small_model = small_model
        self.large_model = large_model
        self.actor_critic_iterations = actor_critic_iterations
        self.yaml_generator_llm = ChatOpenAI(model=large_model)
        self.inference_dir = None
        self.k8s_yaml_dir = None

    def get_k8s_parameters(self):
        """Collect Kubernetes deployment parameters from user."""
        params = {}
        print("\n📦 Let's collect some Kubernetes deployment information:")

        params["app_name"] = input("Enter application name (e.g., iris-inference-api): ").strip()
        params["docker_image"] = input("Enter Docker image name (e.g., username/imagename:tag): ").strip()
        params["container_port"] = input("Enter container port to expose (e.g., 8000): ").strip()
        params["replicas"] = input("Enter number of replicas (pods) you want (e.g., 2): ").strip()
        self.k8s_yaml_dir = input("Enter directory where you want to save Kubernetes YAML files (e.g., ./k8s_files): ").strip()

        print("\n✅ Parameters collected successfully.\n")
        return params

    def generate_inference_script(self):
        pass

    def generate_requirements_txt(self):
        pass

    def generate_dockerfile(self):
        pass

    def docker_build_push(self):
        pass

    def generate_k8s_yamls(self, params, feedback=None):
        """Use LLM to generate Kubernetes deployment and service YAMLs."""
        if feedback is None:
            messages = [
                {"role": "system", "content": "You are a Kubernetes YAML generation expert."},
                {"role": "user", "content": f"""
Generate Kubernetes YAMLs for deploying a FastAPI app.

## Requirements:
- App Name: {params['app_name']}
- Docker Image: {params['docker_image']}
- Container Port: {params['container_port']}
- Number of Replicas: {params['replicas']}

## Constraints:
- Create a deployment.yaml and a service.yaml
- Service type should be ClusterIP (default)
- Expose the container on the specified port
- Follow Kubernetes best practices
- Output both files separately as ```yaml code blocks
- Ensure YAMLs are production-ready
"""}
            ]
        else:
            messages = feedback     

        response = self.yaml_generator_llm.invoke(messages)
        return response

    def extract_and_save_yaml_files(self, llm_response: str):
        """Extracts YAML code blocks from LLM response and saves them into files."""
        llm = ChatOpenAI(model="gpt-4o-mini")

        tools = [save_file_tool]

        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.OPENAI_FUNCTIONS,
            verbose=True,
        )

        response = agent.invoke(
            f"""
            1. Extract all Kubernetes YAML code blocks from the given text.
            2. Save them separately as:
                - deployment.yaml
                - service.yaml
            3. Save them inside this folder: {self.k8s_yaml_dir}
            4. Use the `save_file_tool` to save the content.
            5. Do not output anything else except confirming saving.

            ### Text:
            {llm_response}
            """
        )
        return response

    def apply_k8s_yamls(self):
        """Apply Kubernetes YAML files using kubectl."""
        print(f"🚀 Applying Kubernetes YAMLs from folder: {self.k8s_yaml_dir}...")
        try:
            subprocess.run(f"kubectl apply -f {self.k8s_yaml_dir}", shell=True, check=True)
            print("✅ Kubernetes resources created successfully!")
        except subprocess.CalledProcessError as e:
            print("❌ Error applying Kubernetes YAMLs.")
            print(e)

    def deploy_kubernetes(self):
        """Orchestrates the full Kubernetes deployment process."""
        params = self.get_k8s_parameters()
        raw_yaml_response = self.generate_k8s_yamls(params)
        self.extract_and_save_yaml_files(raw_yaml_response)
        self.apply_k8s_yamls()
