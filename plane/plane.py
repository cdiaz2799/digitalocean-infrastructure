"""A DigitalOcean Python Pulumi program"""

import pulumi
import pulumi_digitalocean as do

# Import Resources
from plane.project import project
from master.vpc import vpc

# Define Vars
region = "sfo3"
ansible_ssh_key = "39220637"

# Create VM
vm1 = do.Droplet(
    "plane-vm-1",
    name="plane-vm-1",
    image="ubuntu-22-04-x64",
    region=region,
    size="s-1vcpu-1gb",
    droplet_agent=True,
    monitoring=True,
    ssh_keys=[ansible_ssh_key],
    vpc_uuid=vpc.id,
    tags=["docker", "plane"],
)

# Create Reserved IP
vm1_ip = do.ReservedIp(
    "plane-vm1-ip",
    region=region,
    droplet_id=vm1.id,
)
# Bind Resources to Project
project_resources = do.ProjectResources(
    "plane-project-resources",
    project=project.id,
    resources=[
        vm1.droplet_urn,
    ],
)
