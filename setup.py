#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# setup.py
# NannoKit.Composer
# © 2026 Heitor Bisneto
#

from setuptools import setup, find_packages

# Ler o README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Project metadata and configuration
setup(
    name="nannokit_composer",                          # Public name of the package
    version="0.0.0",                                    # Version number
    author="Heitor Bisneto",
    author_email="heitor.bardemaker@live.com",
    description="Official Project Generator for SuperNanno Extensions and Modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD-3-Clause",
    url="https://github.com/hbisneto/NannoKit.Composer",   # Homepage URL
    project_urls={
        "Homepage": "https://github.com/hbisneto/NannoKit.Composer",
        "Repository": "https://github.com/hbisneto/NannoKit.Composer.git",
        "Issues": "https://github.com/hbisneto/NannoKit.Composer/issues",
    },
    # Python package discovery
    packages=find_packages(where="."),

    # Scripts / Entrypoints
    entry_points={
        "console_scripts": [
            "nannokitc = nannokit_composer.cli:main",   # Generates the "nannokit_composer" command for CLI usage
        ],
    },

    # Requirements
    install_requires=[
        "filesystempro==3.0.0.0",
    ],

    # Extra requirements (tests, dev etc.)
    extras_require={
        "dev": ["pytest>=7.0.0"],   # Development dependencies
    },

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],

    python_requires=">=3.10",   # Require Python >= 3.10
    keywords=[
        "text-editor", "terminal", "tui", "composer", "nano", 
        "textual", "tree-sitter", "syntax-highlighting", "nannokit"
    ],

    # Automatically include extra files on sdist/wheel
    include_package_data=True,
)