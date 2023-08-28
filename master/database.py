import pulumi
import pulumi_digitalocean as digitalocean
from master.project import master_project
from master.vpc import vpc

# Define Vars

enabled_engines = ["pg"]  # pg,mysql,redis,mongodb
region = "sfo3"
size = "db-s-1vcpu-1gb"

# Define engine versions
engine_versions = {
    "pg": "15",
    "mysql": "8",
    "mongodb": "6",
    "redis": "7",
}

for engine in enabled_engines:
    # Get engine version
    version = engine_versions.get(engine)
    cluster = digitalocean.DatabaseCluster(
        f"{engine}-cluster",
        name=f"{engine}-cluster",
        project_id=master_project.id,
        engine=engine,
        node_count=1,
        region=region,
        size=size,
        version=version,
        private_network_uuid=vpc.id,
    )
