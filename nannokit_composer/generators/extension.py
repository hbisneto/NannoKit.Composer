from pathlib import Path
from ..templates import EXTENSION_TEMPLATE
from .structure import create_structure

class ExtensionGenerator:
    def __init__(self, name):
        self.name = name
        self.project_name = (
            f"NannoKit.{name}"
        )

        self.package = (
            f"nannokit_{name.lower()}"
        )

    def create(self):
        location = (
            Path.home()
            /
            "Documents"
            /
            self.project_name
        )

        location.mkdir(
            parents=True,
            exist_ok=True
        )

        create_structure(
            location,
            EXTENSION_TEMPLATE,
            {
                "project_name":
                    self.project_name,
                "package":
                    self.package,
                "name":
                    self.name.lower()
            }
        )
        return location