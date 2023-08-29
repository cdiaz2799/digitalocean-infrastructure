import pulumi
import pulumi_digitalocean as do

from master.database import cluster as db
from master.vpc import vpc as vpc
from outline.droplet import outline_vm

# Define Database
outline_db = do.DatabaseDb(
    "outline-db",
    cluster_id=db.id,
    name="outline",
    opts=pulumi.ResourceOptions(depends_on=[db])
)

# Define Database User
outline_db_user = do.DatabaseUser(
    "outline-db-user",
    cluster_id=db.id,
    name="outline"
)

# Define Connections Rules
outline_db_fw = do.DatabaseFirewall(
    "outline-db-fw",
    cluster_id=db.id,
    rules=[
        do.DatabaseFirewallRuleArgs(
            type="droplet",
            value=outline_vm.id,
        ),
    ])
