import pulumi_digitalocean as do

# Setup Project
project = do.Project(
    "outline",
    name="outline",
    description="Outline Wiki",
    environment="Production",
    purpose="Web Application",
)
