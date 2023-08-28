import pulumi
import pulumi_cloudflare as cloudflare
from plane.plane import vm1

zone = cloudflare.get_zone(name="cdiaz.cloud")

dns_record = cloudflare.Record(
    "plane-dns",
    name="plane",
    type="A",
    zone_id=zone.zone_id,
    proxied=True,
    value=vm1.ipv4_address,
    opts=pulumi.ResourceOptions(depends_on=[vm1]),
)

pulumi.export("plane-dns", dns_record.hostname)