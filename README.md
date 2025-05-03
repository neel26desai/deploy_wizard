# Deploy_wizard for Kubernetes:

---

## 🌟 Features

- CLI wizard to collect user inputs (Application Name, Docker Image, Port, Replicas)
- Automatic YAML (Deployment + Service) generation via LLM
- Saves YAMLs to a specified folder
- Applies YAMLs automatically with `kubectl`
- Local testing with Minikube supported
- Fast, simple, professional Kubernetes deployments

---

## 📋 Prerequisites

- Python 3.8 or higher
- `kubectl` installed and configured
- Minikube installed and running (for local testing)
- OpenAI API Key (for LLM generation)

## 🚀 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/deploy-wizard.git
cd deploy-wizard
git checkout kubernetes_deployment
```
2. Set up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install Required Python Packages
```
pip install -r requirements.txt
```
4. Export your OpenAI API Key
```
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxx"

```
5. Start Minikube (for local testing)
```
minikube start
```
---
## 🧠 How to Use the Deploy Wizard

1. Run the CLI Wizard

```
python deploy_wizard.py
```
2. Answer the questions in the terminal
   

<img width="708" alt="Screenshot 2025-05-02 at 12 24 16 AM" src="https://github.com/user-attachments/assets/e3bb3545-3bf9-431c-bda8-e3141336a12d" />

3. 🐳 Docker Commands

```
docker build -t mansiiv/iris-llm:latest iris_model_inference
```
Test locally (optional)
```
docker run -p 8000:8000 mansiiv/iris-llm:latest
```
✅ Push to DockerHub

```
docker push mansiiv/iris-llm:latest
```

6. Access the Application
```
minikube service iris-llm-service --url
```
Use /predict with input:

{
  "sepal_length": 5.1,
  
  "sepal_width": 3.5,
  
  "petal_length": 1.4,
  
  "petal_width": 0.2
  
}

You should receive:

{"prediction": 0}



⚡ Notes
Make sure Minikube cluster is running before deploying.

Make sure Docker images you want to deploy are publicly accessible.

The wizard fully automates YAML generation and application — no manual Kubernetes files needed.


