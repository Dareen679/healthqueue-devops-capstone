variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "environment" {
  type    = string
  default = "demo"
}

variable "name_suffix" {
  type        = string
  description = "Globally unique lowercase suffix for S3 name"
}
