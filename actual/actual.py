"""A DigitalOcean Python Pulumi program"""

import pulumi
import pulumi_digitalocean as do
import pulumi_cloudflare as cloudflare


# Setup Project
project = do.Project(
    "actual-budget",
    name="actual-budget",
    description="Actual Budget",
    environment="Production",
    purpose="Web Application",
)
region = "sfo"
ansible_ssh_key = "39220637"

# Create App
actual1 = do.App(
    "actual-1",
    spec=do.AppSpecArgs(
        name="actual-1",
        region=region,
        domain_names=[
            do.AppSpecDomainNameArgs(name="actual.cdiaz.cloud", type="PRIMARY")
        ],
        services=[
            do.AppSpecServiceArgs(
                name="actual-service",
                instance_count=1,
                instance_size_slug="basic-xxs",
                image=do.AppSpecServiceImageArgs(
                    registry_type="DOCKER_HUB",
                    registry="actualbudget",
                    repository="actual-server",
                    tag="latest",
                ),
                http_port=80,
                internal_ports=[5006],
            )
        ],
    ),
)

actual_hostname = actual1.default_ingress.apply(lambda url: url.replace("https://", ""))

project_attachment = do.ProjectResources(
    "project-attachment", project=project.id, resources=[actual1.app_urn]
)

# DNS Record
config = pulumi.Config()
zone = cloudflare.get_zone(name="cdiaz.cloud")

dns_record = cloudflare.Record(
    "actual",
    name="actual",
    type="CNAME",
    zone_id=zone.zone_id,
    proxied=True,
    value=actual_hostname,
    opts=pulumi.ResourceOptions(depends_on=[actual1]),
)


pulumi.export("app", actual1.live_url)
