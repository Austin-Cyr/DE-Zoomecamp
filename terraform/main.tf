terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "8.11.0"
    }
  }
}


provider "google" {
  project = "taxi-rides-ny-514512"
  region  = "us-central1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "taxi-rides-ny-514512-terra-bucket"
  location = "us-central1"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

