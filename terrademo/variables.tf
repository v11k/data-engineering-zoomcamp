variable "project" {
    description = "Project"
    default = "project-312c46a2-5c11-4dab-b73"
}


variable "gcs_bucket_name" {
  description = "Google Cloud Storage Bucket name variable"
  default     = "project-312c46a2-5c11-4dab-b73-terra-bucket"

}

variable "bq_dataset_name" {
  description = "bigquery dataset name"
  default     = "demo_dataset"

}

variable "location" {
  description = "location code variable"
  default     = "EU"

}

variable "gsc_storage_class" {
  description = "Google Cloud Storage Bucket class variable"
  default     = "STANDARD"
}

