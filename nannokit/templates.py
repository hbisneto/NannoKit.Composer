from .core import files

EXTENSION_TEMPLATE = {
    "README.md": files.readme_file,
    "LICENSE": files.license_file,
    "CHANGELOG.md": files.changelog_file,
    "requirements.txt": files.requirements_file,
    "examples": {
        "demo_app.py": files.example_demo_app_file
    },
    "pyproject.toml": files.pyproject_toml_file,
    "setup.py": files.setup_file,
    "nannokit": {
        # "__init__.py": "",
        "app.py": files.nannokit_app_file,
        "demo_app.py": files.nannokit_demo_app_file,
        "{name}": {
            "__init__.py": files.module_init_file,
            "test_main.py": files.module_test_main_file
        }
    },
    "tests": {
        "__init__.py": files.tests_init__file,
        "conftest.py": files.tests_conftest_file,
        "test_main.py": files.tests_main_file
    }
}