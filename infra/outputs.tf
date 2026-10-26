output "audit_bucket" { value = aws_s3_bucket.audit.id }
output "appointments_table" { value = aws_dynamodb_table.appointments_metadata.name }
