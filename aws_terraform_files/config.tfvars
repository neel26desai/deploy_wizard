aws_region = "us-east-1"  # Your selected AWS region
ami_id = "ami-014d544cfef21b42d"  # Your selected AMI ID (or use dynamic fetching)
subnet_id = "subnet-0594e297a19a00930"  # Your subnet ID
key_name = "dw_test"  # Your SSH key name for accessing the instance

# Docker image for model deployment
docker_image = "mansiiv/iris_model_inference:latest"  # Replace with your image in Docker Hub
container_name = "iris_model"  # Container name for the Docker container

# Security group and access control
ssh_cidr_block = "0.0.0.0/0"  # Allow SSH from any IP (replace with your IP for more security)
http_cidr_block = "0.0.0.0/0"  # Allow HTTP from any IP (restrict as needed)
https_cidr_block = "0.0.0.0/0"  # Allow HTTPS from any IP (restrict as needed)
model_cidr_block = "0.0.0.0/0"  # Allow access to the model from any IP (adjust based on need)

# Resource naming
resource_prefix = "iris"  # Prefix for the names of resources (EC2, SG, etc.)

# Override any other variable defaults as needed
