import pulumi
import pulumi_digitalocean as digitalocean
import pulumi_cloudflare as cloudflare
from master.vpc import vpc


# Define Vars
app_name = "opconnect"
region = "sfo3"
ansible_ssh_key = "39220637"
tags = [
    app_name,
]

# Droplet
opconnect_vm1 = digitalocean.Droplet(
    "opconnect-vm1",
    image="rockylinux-9-x64",
    name=f"{app_name}-vm1",
    region=region,
    size="s-1vcpu-512mb-10gb",
    tags=tags,
    vpc_uuid=vpc.id,
    opts=pulumi.ResourceOptions(protect=True),
)

# Firewall
opconnect_fw = digitalocean.Firewall(
    "opconnect-fw",
    droplet_ids=[opconnect_vm1.id],
    inbound_rules=[
        digitalocean.FirewallInboundRuleArgs(
            port_range="22",
            protocol="tcp",
            source_addresses=[
                "0.0.0.0/0",
                "::/0",
            ],
        ),
        digitalocean.FirewallInboundRuleArgs(
            port_range="8080",
            protocol="tcp",
            source_addresses=[
                "0.0.0.0/0",
                "::/0",
            ],
        ),
    ],
    outbound_rules=[
        digitalocean.FirewallOutboundRuleArgs(
            destination_addresses=[
                "0.0.0.0/0",
                "::/0",
            ],
            port_range="all",
            protocol="udp",
        ),
        digitalocean.FirewallOutboundRuleArgs(
            destination_addresses=[
                "0.0.0.0/0",
                "::/0",
            ],
            protocol="icmp",
        ),
        digitalocean.FirewallOutboundRuleArgs(
            destination_addresses=[
                "0.0.0.0/0",
                "::/0",
            ],
            port_range="all",
            protocol="tcp",
        ),
    ],
)

# DNS Record
zone = cloudflare.get_zone(name="cdiaz.cloud")
dns_record = cloudflare.Record(
    "opconnect-dns",
    name=app_name,
    type="A",
    zone_id=zone.zone_id,
    proxied=False,
    value=opconnect_vm1.ipv4_address,
    opts=pulumi.ResourceOptions(depends_on=[opconnect_vm1]),
)

pulumi.export("opconnect-dns", dns_record.hostname)
