# AWS Region
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"  # Change as needed
}

# AMI ID (will dynamically fetch latest Amazon Linux 2 AMI if left empty)
variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = ""  # Empty, will fetch dynamically if not provided
}

# Instance Type (default t2.micro for free tier)
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"  # Free tier eligible instance
}

# Subnet ID (can be provided or default to the region's default subnet)
variable "subnet_id" {
  description = "Subnet ID where the instance will be launched"
  type        = string
  default     = ""  # Empty, will fetch dynamically if not provided
}

# SSH Key Name
variable "key_name" {
  description = "SSH key pair name for accessing the instance"
  type        = string
  default     = "dw_test"  # Replace with your SSH key name
}

# Docker Image for model deployment
variable "docker_image" {
  description = "Docker image for model deployment"
  type        = string
  default     = "mansiiv/iris_model_inference:latest"
}

# Docker container name
variable "container_name" {
  description = "Name of the Docker container"
  type        = string
  default     = "iris_model"
}

# Resource prefix for naming
variable "resource_prefix" {
  description = "Prefix for resource naming"
  type        = string
  default     = "iris"
}

# CIDR blocks for SSH, HTTP, HTTPS access
variable "ssh_cidr_block" {
  description = "CIDR block for SSH access"
  type        = string
  default     = "0.0.0.0/0"  # Replace with your actual IP address
}

variable "http_cidr_block" {
  description = "CIDR block for HTTP access"
  type        = string
  default     = "0.0.0.0/0"
}

variable "https_cidr_block" {
  description = "CIDR block for HTTPS access"
  type        = string
  default     = "0.0.0.0/0"
}

# Model access CIDR block
variable "model_cidr_block" {
  description = "CIDR block for model access"
  type        = string
  default     = "0.0.0.0/0"
}
