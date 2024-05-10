output "cluster_name" {
  value = google_container_cluster.primary.name
}

output "endpoint" {
  value = google_container_cluster.primary.endpoint
}

output "master_auth" {
  sensitive = true
  value = google_container_cluster.primary.master_auth
}

output "load_balancer_ip" {
  value       = google_container_cluster.primary.endpoint # Modify this to fetch the actual LB IP if needed
  description = "Load balancer IP for Argo CD"
}
