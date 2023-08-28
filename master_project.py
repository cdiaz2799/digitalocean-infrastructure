import pulumi
import pulumi_digitalocean as digitalocean

master_project = digitalocean.Project(
    "master",
    environment="Production",
    is_default=True,
    name="master",
    purpose="Operational / Developer tooling",
    opts=pulumi.ResourceOptions(protect=True),
)
