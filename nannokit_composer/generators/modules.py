from pathlib import Path

class ModuleGenerator:
    def __init__(self,name):
        self.name=name
    def create(self):
        base = (
            Path.home()
            /
            "Documents"
            /
            "NannoKit"
            /
            self.name
        )
        base.mkdir(
            parents=True,
            exist_ok=True
        )
        (base/"__init__.py").write_text(
            ""
        )
        return base