from paperless.project import paperless_project as project
import pulumi
import pulumi_digitalocean
from pulumi_digitalocean import Droplet, ReservedIp
from master.vpc import vpc

app_name = "paperless"
region = "sfo3"
ansible_ssh_key = "39220637"
tags = [
    app_name,
]

# Setup Droplet
paperless_vm = Droplet(
    resource_name="paperless-vm",
    name=f"{app_name}-vm-1",
    image="rockylinux-9-x64",
    region=region,
    size="s-1vcpu-1gb",
    droplet_agent=True,
    monitoring=True,
    ssh_keys=[ansible_ssh_key],
    vpc_uuid=vpc.id,
    tags=tags,
)
