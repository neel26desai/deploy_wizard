variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-1"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-08d4f6bbae664bd41"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro" # Consider evaluating instance type for production workloads
}

variable "subnet_id" {
  description = "Subnet ID where the instance will be launched"
  type        = string
  default     = "subnet-070d54662e68443ed"
}

variable "key_name" {
  description = "SSH key pair name for accessing the instance"
  type        = string
  default     = "neel_test"
}

variable "docker_image" {
  description = "Docker image for model deployment"
  type        = string
  default     = "neel26d/iris_model_inference:latest"
}

variable "container_name" {
  description = "Name of the Docker container"
  type        = string
  default     = "iris_model"
}

variable "resource_prefix" {
  description = "Prefix for resource naming"
  type        = string
  default     = "iris"
}

variable "ssh_cidr_block" {
  description = "CIDR block for SSH access"
  type        = string
  default     = "0.0.0.0/0" # Replace with your actual IP address
}

variable "http_cidr_block" {
  description = "CIDR block for HTTP access"
  type        = string
  default     = "0.0.0.0/0" # Change as needed
}

variable "https_cidr_block" {
  description = "CIDR block for HTTPS access"
  type        = string
  default     = "0.0.0.0/0" # Change as needed
}

variable "model_cidr_block" {
  description = "CIDR block for model access"
  type        = string
  default     = "0.0.0.0/0" # Change as needed
}