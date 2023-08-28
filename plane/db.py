import pulumi
import pulumi_digitalocean as do

from master.database import cluster as db
from plane.plane import vm1 as vm1

# Define Database
plane_db = do.DatabaseDb(
    "plane-db",
    cluster_id=db.id,
    name="plane",
    opts=pulumi.ResourceOptions(depends_on=[db])
)

# Define Database User
plane_db_user = do.DatabaseUser(
    "plane-db-user",
    cluster_id=db.id,
    name="plane"
)

# Define Connections Rules
plane_db_fw = do.DatabaseFirewall(
    "plane-db-fw",
    cluster_id=db.id,
    rules=[
        do.DatabaseFirewallRuleArgs(
            type="droplet",
            value=vm1.id,
        ),
    ])
