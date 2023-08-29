import pulumi_digitalocean as do
from master.vpc import vpc
from outline.project import project

# Define Vars
app_name = "outline"
region = "sfo3"
ansible_ssh_key = "39220637"

# Retrieve cloud-init file
with open('outline/cloud-init.yaml', 'r') as file:
    cloud_init = file.read()

# Define VM
outline_vm = do.Droplet(
    f"{app_name}-vm-1",
    name=f"{app_name}-vm-1",
    image="ubuntu-22-04-x64",
    region=region,
    size="s-1vcpu-1gb",
    droplet_agent=True,
    monitoring=True,
    ssh_keys=[ansible_ssh_key],
    user_data=cloud_init,
    vpc_uuid=vpc.id,
)

# Define IP Reservation
outline_vm_ip = do.ReservedIp(
    f"{app_name}-reservation",
    region=region,
    droplet_id=outline_vm.id,
)

# Add Resources to Project
outline_project = do.ProjectResources(
    f"{app_name}-project-resources",
    project=project.id,
    resources=[
        outline_vm.droplet_urn,
    ]
)
