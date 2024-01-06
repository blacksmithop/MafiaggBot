from setuptools import setup
import re

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = ""
with open("mafiagg/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("version is not set")


readme = ""
with open("readme.md") as f:
    readme = f.read()

extras_require = {
    "docs": [
        "mkdocs-material==9.5.3",
    ]
}

packages = ["mafiagg", "mafiagg.bot", "mafiagg.helper", "mafiagg.models"]

setup(
    name="mafiagg",
    author="blacksmithop",
    url="https://github.com/blacksmithop/MafiaggBot",
    project_urls={
        "Documentation": "https://blacksmithop.github.io/MafiaggBot/",
        "Issue tracker": "https://github.com/blacksmithop/MafiaggBot/issues",
    },
    version=version,
    packages=packages,
    license="MIT",
    description="A Python wrapper for the MafiaGG API",
    long_description=readme,
    long_description_content_type="text/md",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires=">=3.8.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
