"""A DigitalOcean Python Pulumi program"""

import pulumi
import pulumi_digitalocean as do

# Define Vars
vpc_name_fmt = "cdiaz-cloud-vpc"
regions = ["sfo3"]

# Create VPC(s)
vpcs = []
for region in regions:
    vpc_name = f"{vpc_name_fmt}-{region}"
    vpc = do.Vpc(
        f"{vpc_name}",
        name=vpc_name,
        region=region,
    )
    vpcs.append(vpc)
