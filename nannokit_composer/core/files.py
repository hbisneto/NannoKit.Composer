readme_file = """# NannoKit.{name}

**Official {name} extension for SuperNanno** — Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

NannoKit.{name} provides clean, high-level APIs for common user interactions, inspired by modern desktop application patterns.

> Designed to integrate seamlessly into **SuperNanno** and work standalone in any Textual app.

---

## ✨ Features

- Automatic resolution of the running Textual `App` (no manual passing required in most cases)
- Full keyboard and mouse support
- Consistent behavior: Escape to cancel
- Internal composition between components
- Full test coverage with Textual Pilot
- Installable as a standalone package or as part of the SuperNanno ecosystem
- Modern and clean API design

---

## 📦 Installation

```bash
pip install nannokit-{name}
```

To also install with SuperNanno (when available):

```bash
pip install "nannokit-{name}[supernanno]"
```

---

## 🚀 Quick Start

```python
from nannokit.{name} import example_class_1, example_class_2
from pathlib import Path

# Example usage
example_class_1.show(
    # parameters here
    callback=lambda result: print("Result:", result),
)

# Another example
example_class_2.show(
    title="Example Title",
    callback=lambda value: print("Value:", value),
)
```

---

## Integration with SuperNanno

In your main `App` class, attach the manager once (recommended):

```python
from textual.app import App
from nannokit.{name}.core import manager_class

class SuperNannoApp(App):
    def on_mount(self) -> None:
        manager_class.attach(self)
        # ... rest of your app
```

After this setup, you can call any {name} component from anywhere in your application.

---

## 📖 API

### Main Components

- **`main_class_1.show(...)`** — Lorem ipsum dolor sit amet, consectetur adipiscing elit.
- **`main_class_2.show(...)`** — Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
- **`main_class_3.show(...)`** — Ut enim ad minim veniam, quis nostrud exercitation.

All components accept common parameters such as `title`, `initial_value`, `callback`, and `show_hidden`.

### section_name

```python
section_example
```

---

## Package Structure

```
nannokit/{name}/
├── core/              # Shared manager, base classes and utilities
├── module_1/        # module_1_description
├── module_2/        # module_2_description
├── module_3/        # module_3_description
└── styles/            # TCSS stylesheets
```

---

## Development

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for recent changes (architecture refactor, bug fixes, new features, end-to-end tests, etc.).

---

## License

**BSD 3-Clause License** — see the [LICENSE](LICENSE) file for details.

---

**Part of the [SuperNanno](https://github.com/hbisneto/SuperNanno) ecosystem.**

Built to make Textual application development even more powerful and enjoyable.

**Author:** Heitor Bardemaker A. Bisneto (@BisnetoDev)
"""

license_file = """BSD 3-Clause License

Copyright (c) 2026, Heitor Bardemaker A. Bisneto

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

changelog_file = """NannoKit.{name} Changelog:
"""

requirements_file = """linkify-it-py==2.1.0
markdown-it-py==4.2.0
mdit-py-plugins==0.6.1
mdurl==0.1.2
platformdirs==4.10.0
Pygments==2.20.0
rich==15.0.0
textual==8.2.7
typing_extensions==4.15.0
uc-micro-py==2.0.0
"""

example_demo_app_file = """# NannoKit.{name} Demo App:
"""

pyproject_toml_file = """[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "nannokit-{name}"
version = "0.0.0"
description = "Official {name} extension for SuperNanno"
readme = "README.md"
license = {text = "BSD-3-Clause"}
authors = [{name = "Heitor Bardemaker A. Bisneto", email = "bisnetoinc@gmail.com"}]
requires-python = ">=3.10"
dependencies = ["textual>=8.2.7"]

[tool.setuptools.packages.find]
include = ["nannokit*"]
namespaces = true

[tool.setuptools.package-data]
"nannokit.dialogs.styles" = ["*.tcss"]
"""

setup_file = """# -*- coding: utf-8 -*-
from setuptools import setup, find_namespace_packages

setup(
    name="nannokit_{name}",
    version="0.0.0",
    description="Official {name} extension for SuperNanno",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Heitor Bardemaker A. Bisneto",
    author_email="bisnetoinc@gmail.com",
    license="BSD-3-Clause",
    url="https://github.com/hbisneto/SuperNanno",

    packages=find_namespace_packages(include=["nannokit*"]),
    include_package_data=True,
    package_data={
        "nannokit.{name}.styles": ["*.tcss"],
    },

    install_requires=["textual>=8.2.7"],
    python_requires=">=3.10",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Text Editors",
        "Typing :: Typed",
    ],

    zip_safe=False,
)
"""

nannokit_app_file = """
# supernanno/app.py
#
# Example of how the SuperNanno main App integrates with {name}.
#
# The App must call DialogManager.attach(self) once — typically in on_mount.
# After that, {name} works anywhere without passing `app` manually.

from textual.app import App, ComposeResult
from textual.widgets import Label
from {name}.core.manager import DialogManager

class SuperNannoApp(App):
    def on_mount(self) -> None:
        DialogManager.attach(self)

    def compose(self) -> ComposeResult:
        yield Label("{name} — Press D to run the example")

    def on_key(self, event) -> None:
        if event.key == "d":
            self._demo_dialog()

    def _demo_dialog(self) -> None:
        def resposta(btn: str) -> None:
            self.notify(f"User clicked a button")

if __name__ == "__main__":
    SuperNannoApp().run()
"""

nannokit_demo_app_file = """
"""

module_init_file = """
"""

module_test_main_file = """
"""

tests_init__file = """
"""

tests_conftest_file = """
"""

tests_main_file = """
"""