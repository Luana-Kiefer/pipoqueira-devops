terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Grupo de Segurança para liberar a porta da pipoqueira
resource "aws_security_group" "pipoqueira_sg" {
  name        = "pipoqueira-devops-sg"
  description = "Grupo de seguranca para a aplicação Pipoqueira DevOps"

  ingress {
    description      = "Porta da aplicação Flask"
    from_port        = 5000
    to_port          = 5000
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "Acesso SSH"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "PipoqueiraDevOps-SG"
  }
}

# Instância EC2 na AWS
resource "aws_instance" "pipoqueira_server" {
  ami           = "ami-0c7217cdde317cfec" # Ubuntu Server na us-east-1
  instance_type = "t2.micro"

  security_groups = [aws_security_group.pipoqueira_sg.name]

  tags = {
    Name = "PipoqueiraDevOps-Server"
  }
}