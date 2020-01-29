#!/usr/bin/env python3

import os

provider = """provider "aws" {
  version = "~> 2.0"
  region  = var.region
}
"""

backend = """terraform {
  backend "s3" {}
}
"""
variables = """variable "environment" {}
variable "region" {}
"""

tfvars = """environment = ""
region      = ""
"""

backend_config = """bucket=""
dynamodb_table=""
region=""
key=""
"""

f = open(os.getcwd() + "/variables.tf", "w+")
f.write(variables)
f.close()
f = open(os.getcwd() + "/backend.tf", "w+")
f.write(backend)
f.close()
f = open(os.getcwd() + "/provider.tf", "w+")
f.write(provider)
f.close()
f = open(os.getcwd() + "/staging.tfvars", "w+")
f.write(tfvars)
f.close()
f = open(os.getcwd() + "/production.tfvars", "w+")
f.write(tfvars)
f.close()
f = open(os.getcwd() + "/staging.backend", "w+")
f.write(backend_config)
f.close()
f = open(os.getcwd() + "/production.backend", "w+")
f.write(backend_config)
f.close()

extra_files = ["main.tf", 
    "data.tf"]

for element in extra_files:
    f = open(os.getcwd() + "/" + element, "w+")
    f.close()