from setuptools import setup, find_packages

setup(
    name="update-docs",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "update-docs = update_docs.cli:main"
        ]
    },
    author="CoreTwin System",
    description="CLI tool for maintaining Markdown documentation structure and include references.",
    install_requires=[],
    python_requires='>=3.7',
)
