from pulumi import ComponentResource, ResourceOptions, export
from pulumi_digitalocean import Project


class AppProject(ComponentResource):
    def __init__(self, name: str, app_name: str, opts=None):
        super().__init__("my:modules:AppProject", name, None, opts)

        self.do_project = Project(
            f"{app_name}-project",
            name=app_name,
            description=f"{app_name} Resources",
            environment="Development",
            is_default=False,
            opts=ResourceOptions(parent=self),
        )

        self.register_outputs({"appProjectUrn": self.do_project.urn})
