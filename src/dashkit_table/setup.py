import json
from pathlib import Path

from setuptools import setup

# Read metadata from package-info.json
package_json = json.loads(
    (Path(__file__).parent / "dashkit_table" / "package-info.json").read_text()
)

setup(
    name="dashkit_table",
    version="1.1.2",
    description="Modern Handsontable component for Dash with native theming support",
    long_description=(Path(__file__).parent / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/dashkit_table/",
    project_urls={
        "Homepage": "https://pypi.org/project/dashkit_table/",
        "Source": "https://github.com/iamgp/dash-attio",
        "Issues": "https://github.com/iamgp/dash-attio/issues",
    },
    packages=["dashkit_table"],
    include_package_data=True,
    package_data={
        "dashkit_table": [
            "*.js",
            "*.js.map",
            "*.json",
            "*.txt",
            "*.py",
        ]
    },
    python_requires=">=3.8",
    install_requires=[
        "dash>=2.0.0",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: Dash",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
    ],
    author="Dashkit Team",
    license="MIT",
    license_files=["LICENSE"],
)
