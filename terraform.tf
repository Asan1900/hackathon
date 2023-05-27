provider "aws" {
  access_key = "<your-access-key>"
  secret_key = "<your-secret-key>"
  region     = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c94855ba95c71c99"
  instance_type = "t2.micro"
}

output "instance_ip" {
  value = aws_instance.example.public_ip
}

