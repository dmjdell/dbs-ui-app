variable "project_id" {
  description = "GCP Project ID"
  type        = string
  default     = "rapid-strength-422813-t9"
}

variable "region" {
  description = "GCP region to create the cluster"
  type        = string
  default     = "us-central1"
}

variable "cluster_name" {
  description = "Name of the GKE cluster"
  type        = string
  default     = "dennis-cluster"
}

variable "argocd_version" {
  description = "Version of the Argo CD Helm chart"
  type        = string
  default     = "5.48.0"
}

variable "argo_rollouts_version" {
  description = "Version of the Argo Rollouts Helm chart"
  type        = string
  default     = "1.6.0"
}
