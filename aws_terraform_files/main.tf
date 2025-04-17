provider "aws" {
  region = var.aws_region
}

# Fetch the latest Amazon Linux AMI dynamically
data "aws_ami" "latest_ami" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]  # Adjust this filter as needed for the desired AMI
  }
}

resource "aws_security_group" "ec2_sg" {
  name_prefix = "${var.resource_prefix}-sg-"

  # Allow SSH access from a specific IP address
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.ssh_cidr_block] # Ensure this is set to a specific IP
  }

  # Allow HTTP access (consider restricting this as needed)
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = [var.http_cidr_block] # Restrict this as needed
  }

  # Allow HTTPS access (consider restricting this as needed)
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [var.https_cidr_block] # Restrict this as needed
  }

  # Allow requests to come to the model
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = [var.model_cidr_block] # Restrict this as needed
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.resource_prefix}-ec2-sg"
  }
}

resource "aws_instance" "model_server" {
  ami                    = data.aws_ami.latest_ami.id  # Use dynamic AMI ID fetched by the data source
  instance_type           = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids  = [aws_security_group.ec2_sg.id]
  key_name               = var.key_name

  user_data = <<EOF
#!/bin/bash
set -e

# Update and install Docker
if ! command -v docker &> /dev/null; then
  sudo yum update -y
  sudo yum install -y docker
  sudo systemctl start docker
  sudo systemctl enable docker
  sudo usermod -aG docker ec2-user
fi

# Pull the latest Docker image
if ! sudo docker pull ${var.docker_image}; then
  echo "Failed to pull Docker image" | tee -a /var/log/user-data.log
  exit 1
fi

# Run the container
if ! sudo docker run -d -p 8000:8000 --name ${var.container_name} ${var.docker_image}; then
  echo "Failed to run Docker container" | tee -a /var/log/user-data.log
  exit 1
fi

echo "Model server started successfully" | tee -a /var/log/user-data.log
EOF

  tags = {
    Name = "${var.resource_prefix}-model-server"
  }
}

output "model_server_public_ip" {
  value = aws_instance.model_server.public_ip
}

output "model_server_public_dns" {
  value = aws_instance.model_server.public_dns
}
