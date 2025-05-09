variable "resource_group_name" {
  description = "Name of the Resource Group"
  type        = string
  default     = "ruchitha_rg31"
}

variable "location" {
  description = "Azure Region for resources"
  type        = string
  default     = "eastus"
}

variable "virtual_network_name" {
  description = "Name of the Virtual Network"
  type        = string
  default     = "irisruchithavnet31"
}

variable "address_space" {
  description = "Address space for the Virtual Network"
  type        = string
  default     = "10.0.0.0/16"
}

variable "subnet_name" {
  description = "Name of the Subnet"
  type        = string
  default     = "ruchithaasubnet31"
}

variable "subnet_address_prefix" {
  description = "Subnet address prefix"
  type        = string
  default     = "10.0.1.0/24"
}

variable "nsg_name" {
  description = "Name of the Network Security Group"
  type        = string
  default     = "ruchithansg31"
}

variable "public_ip_name" {
  description = "Name of the Public IP"
  type        = string
  default     = "ruchithapublicip31"
}

variable "dns_label" {
  description = "DNS label for Public IP"
  type        = string
  default     = "ruchithadns31"
}

variable "nic_name" {
  description = "Name of the Network Interface"
  type        = string
  default     = "ruchithanic31"
}

variable "vm_name" {
  description = "Name of the VM"
  type        = string
  default     = "RuchithaVM31"
}

variable "admin_username" {
  description = "Admin username for the VM"
  type        = string
  default     = "azureuser31"
}


variable "admin_password" {
  description = "The password for the VM admin user"
  type        = string
  sensitive   = true
}


variable "ssh_public_key_path" {
  description = "Local path to the SSH public key file for key-based authentication"
  type        = string
  default     = "C:/Users/ruchi/.ssh/id_rsa.pub"
}

variable "vm_size" {
  description = "Size of the VM"
  type        = string
  default     = "Standard_B1ls"
}

variable "docker_image" {
  description = "Docker image URI"
  type        = string
  default     = "mcr.microsoft.com/azuredocs/aci-helloworld:latest"
}

variable "container_name" {
  description = "Container name"
  type        = string
  default     = "iris-model31"
}

variable "model_port" {
  description = "Port exposed by the model container"
  type        = number
  default     = 8000
}

variable "image_publisher" {
  description = "VM image publisher"
  type        = string
  default     = "Canonical"
}

variable "image_offer" {
  description = "VM image offer"
  type        = string
  default     = "UbuntuServer"
}

variable "image_sku" {
  description = "VM image SKU"
  type        = string
  default     = "18.04-LTS"
}

variable "allowed_ssh_ip" {
  description = "Allowed IP range for SSH access"
  type        = string
  default     = "0.0.0.0/0"  # Change to a specific IP range for better security
}

variable "allowed_api_ip" {
  description = "Allowed IP range for API access"
  type        = string
  default     = "0.0.0.0/0"  # Change to a specific IP range for better security
}

variable "tags" {
  description = "Tags to be applied to resources"
  type        = map(string)
  default     = {
    environment = "development"
    project     = "iris-model"
  }
}
