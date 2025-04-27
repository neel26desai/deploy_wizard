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
##🧠 How to Use the Deploy Wizard

1. Run the CLI Wizard

```
python deploy_wizard.py
```
2. Answer the questions in the terminal
   
<img width="812" alt="Screenshot 2025-04-26 at 5 46 32 PM" src="https://github.com/user-attachments/assets/71977f29-24cd-4442-9f2d-e6969cb20c68" />

3. Actions taken:

LLM generates deployment.yaml and service.yaml

Saves YAMLs into the specified folder

Applies them automatically with kubectl

Creates Deployment and Service inside Kubernetes

4. Verify the Deployment
```
kubectl get pods
```
5.Check services:
```
kubectl get services
```
6. Access the Application
```
minikube service your-service-name --url
```


⚡ Notes
Make sure Minikube cluster is running before deploying.

Make sure Docker images you want to deploy are publicly accessible.

The wizard fully automates YAML generation and application — no manual Kubernetes files needed.


