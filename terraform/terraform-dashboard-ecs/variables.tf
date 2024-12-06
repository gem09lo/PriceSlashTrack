variable "AWS_ACCESS_KEY" {
  type = string
}
variable "AWS_SECRET_KEY" {
  type = string
}


variable "DB_USER" {
    type = string
}
variable "DB_PASSWORD"{
    type = string
}
variable "DB_NAME" {
    type = string
}
variable "DB_HOST"{
    type = string
}
variable "DB_PORT"{
    type = string
}


variable "DASHBOARD_ECR_NAME"{
    type = string
    description = "ECR that holds the Dashboard."
}