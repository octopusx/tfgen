#!/usr/bin/env python3

import argparse
import os
import sys

app_name = ""
path = ""
region = "eu-central-1"


def write_files():
    global path
    environment = ""

    provider = """provider "aws" {
      version = "~> 2.0"
      region  = var.region
    }
    """

    backend = """terraform {
      backend "s3" {}
    }
    """

    variables = f"""variable "environment" {{}}
    variable "region" {{ default = "{region}" }}
    """

    tfvars = f"""environment = "{environment}"
    """

    backend_config = f"""bucket="around-tfstate-{environment}"
    dynamodb_table="apps/{app_name}/terraform.tfstate"
    region="{region}"
    key="around-tfstate-{environment}"
    """

    f = open(path + "/variables.tf", "w+")
    f.write(variables)
    f.close()
    f = open(path + "/backend.tf", "w+")
    f.write(backend)
    f.close()
    f = open(path + "/provider.tf", "w+")
    f.write(provider)
    f.close()
    f = open(path + "/staging.tfvars", "w+")
    environment = "staging"
    tfvars = f"""environment = "{environment}"
    """
    f.write(tfvars)
    f.close()
    f = open(path + "/production.tfvars", "w+")
    environment = "production"
    tfvars = f"""environment = "{environment}"
    """
    f.write(tfvars)
    f.close()
    f = open(path + "/staging.backend", "w+")
    environment = "staging"
    backend_config = f"""bucket="around-tfstate-{environment}"
      dynamodb_table="apps/{app_name}/terraform.tfstate"
      region="{region}"
      key="around-tfstate-{environment}"
      """
    f.write(backend_config)
    f.close()
    f = open(path + "/production.backend", "w+")
    environment = "production"
    backend_config = f"""bucket="around-tfstate-{environment}"
      dynamodb_table="apps/{app_name}/terraform.tfstate"
      region="{region}"
      key="around-tfstate-{environment}"
      """
    f.write(backend_config)
    f.close()

    extra_files = ["main.tf",
                   "data.tf"]

    for element in extra_files:
        f = open(path + "/" + element, "w+")
        f.close()


# input()
def input():
    global path
    global app_name

    # Create the parser
    my_parser = argparse.ArgumentParser(
        description='Create a skeleton terraform project')

    # Add the arguments
    my_parser.add_argument('Path',
                           metavar='path',
                           type=str,
                           help='the path where the new module will be created')

    my_parser.add_argument('App',
                           metavar='app',
                           type=str,
                           help='the name of the application')

    args = my_parser.parse_args()
    path = args.Path
    app_name = args.App


input()
write_files()
