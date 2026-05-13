variable "subscription_id" {
  description = "Azure subscription ID"
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure resource group"
  type        = string
  default     = "daniel-cicd"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "southeastasia"
}

variable "acr_name" {
  description = "Name of the Azure Container Registry (alphanumeric only)"
  type        = string
  default     = "djangocicdlab"
}

variable "aks_cluster_name" {
  description = "Name of the AKS cluster"
  type        = string
  default     = "django-cicd-aks"
}

variable "node_vm_size" {
  description = "VM size for AKS nodes"
  type        = string
  default     = "Standard_B2s"
}

variable "node_count" {
  description = "Number of AKS nodes"
  type        = number
  default     = 1
}
