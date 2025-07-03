from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="update-docs-system",
    version="1.0.0",
    author="CoreTwin System",
    author_email="support@coretwin.com",
    description="Комплексная система автоматизации документации для проектов с Markdown файлами",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CoreTwin/docs_repo",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements + [
        "click>=8.0.0",
        "gitpython>=3.1.0",
        "watchdog>=2.1.0",
    ],
    entry_points={
        "console_scripts": [
            "update-docs=update_docs.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "update_docs": [
            "templates/*",
        ],
    },
)
