import pulumi_digitalocean as do
from master.project import master_project as project
from master.vpc import vpc as vpc

# Define Vars
app_name = "ansible"
region = "sfo3"
ssh_key = "39244416"
tags = [
    "ansible",
    "docker",
    "gitlab-runner",
]

# Retrieve cloud-init file
with open("master/ansible-cloud-init.yaml", "r") as file:
    cloud_init = file.read()

# Define VM / Droplet
ansible_vm = do.Droplet(
    f"{app_name}-vm-1",
    name=f"{app_name}-vm-1",
    image="ubuntu-22-04-x64",
    region=region,
    size="s-1vcpu-1gb",
    droplet_agent=True,
    monitoring=True,
    ssh_keys=[ssh_key],
    user_data=cloud_init,
    vpc_uuid=vpc.id,
    tags=tags,
)

# Add Resources to Project
ansible_project = do.ProjectResources(
    f"{app_name}-project-resources",
    project=project.id,
    resources=[
        ansible_vm.droplet_urn,
    ],
)
