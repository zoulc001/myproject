resource "aws_ecr_repository" "nginx_webapp" {
    name = "nginx_webapp"
}
provider "aws" {
    region = "ap-southeast-1"
}

