terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = "eu-central-1" # change if needed
}

locals {
  bucket_name = "nyc-taxi-bronze-dev-incremental-load" # must be globally unique
  tags = {
    Project = "nyc-taxi"
    Env     = "dev"
  }
}

resource "aws_s3_bucket" "bronze" {
  bucket = local.bucket_name
  tags   = local.tags
}

# Block all public access (recommended)
resource "aws_s3_bucket_public_access_block" "bronze" {
  bucket                  = aws_s3_bucket.bronze.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Versioning (recommended)
resource "aws_s3_bucket_versioning" "bronze" {
  bucket = aws_s3_bucket.bronze.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Default encryption (recommended)
resource "aws_s3_bucket_server_side_encryption_configuration" "bronze" {
  bucket = aws_s3_bucket.bronze.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

output "bronze_bucket_name" {
  value = aws_s3_bucket.bronze.bucket
}