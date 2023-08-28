import pulumi_digitalocean as do

# Setup Project
project = do.Project(
    "plane",
    name="plane",
    description="Plane Project Management",
    environment="Production",
    purpose="Web Application",
)
