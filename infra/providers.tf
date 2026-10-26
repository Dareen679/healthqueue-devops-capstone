terraform {
  required_version = ">= 1.8.0"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
  # For team usage: configure a remote S3 backend using backend.hcl (see README).
  backend "s3" {}
}
provider "aws" {
  region = var.aws_region
  default_tags { tags = { Project = "HealthQueue", ManagedBy = "OpenTofu", Environment = var.environment } }
}
