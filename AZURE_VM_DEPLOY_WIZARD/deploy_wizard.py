from azure_helper.azure_deploy_wizard import DeployAzureVM

if __name__ == "__main__":
    print("🌐 Where would you like to deploy your model?")
    print("1. AWS EC2")
    print("2. Azure VM")
    print("3. Print Kubernetes")
    print("4. AWS SageMaker")
    print("5. Azure ML")

    user_input = input("Please enter the number corresponding to your choice: ").strip()

    if user_input == "1":
        print("🚀 You have selected AWS EC2.")

    elif user_input == "2":
        print("🚀 You have selected Azure VM.")
        azure_deploy = DeployAzureVM()
        azure_deploy.deploy_azure_vm()

    elif user_input == "3":
        print("⚙️ You have selected Kubernetes.")
        # Placeholder: Add Kubernetes deployment code here

    elif user_input == "4":
        print("⚙️ You have selected AWS SageMaker.")
        # Placeholder: Add SageMaker deployment code here

    elif user_input == "5":
        print("⚙️ You have selected Azure ML.")
        # Placeholder: Add Azure ML deployment code here

    else:
        print("❌ Invalid selection. Please try again.")
