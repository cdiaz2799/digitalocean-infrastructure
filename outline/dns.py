import pulumi
import pulumi_cloudflare as cloudflare
from outline.droplet import outline_vm_ip

zone = cloudflare.get_zone(name="cdiaz.cloud")

dns_record = cloudflare.Record(
    "outline-dns",
    name="outline",
    type="A",
    zone_id=zone.zone_id,
    proxied=True,
    value=outline_vm_ip.id,
    opts=pulumi.ResourceOptions(depends_on=[outline_vm_ip]),
)

pulumi.export("outline-dns", dns_record.hostname)