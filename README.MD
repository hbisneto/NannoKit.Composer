# NannoKit Composer

**Official Project Generator for SuperNanno Extensions and Modules**

A command-line tool that creates the complete structure for `NannoKit` extensions with a single command.

---

## ✨ Features

- Fast creation of complete extensions (`nannokit-{name}`)
- Standardized structure ready for PyPI publication
- Up-to-date templates with SuperNanno ecosystem best practices
- Built-in support for automatic variable substitution (`{name}`)
- Easy integration with Textual + SuperNanno

---

## 📦 Installation

### 1. Clone or download the project

```bash
cd ~/Desktop/Bisneto/Python
git clone https://github.com/hbisneto/NannoKitComposer.git    # if hosted on GitHub
cd NannoKitComposer
```

### Directory Tree

```bash
NannoKitComposer
│
├── nannokit_composer
│   ├── __init__.py
│   ├── cli.py              # CLI commands
│   ├── composer.py         # main logic
│   ├── templates.py        # project templates
│   └── generators
│       ├── __init__.py
│       ├── extension.py
│       └── module.py
│
├── setup.py
└── pyproject.toml
```