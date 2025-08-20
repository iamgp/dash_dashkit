import json
from pathlib import Path

from setuptools import setup

# Read metadata from package-info.json
package_json = json.loads(
    (Path(__file__).parent / "dashkit_kiboui" / "package-info.json").read_text()
)

setup(
    name="dashkit_kiboui",
    version="1.0.1",
    description="Contribution graph components for Dash with native theming support",
    long_description=(Path(__file__).parent / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/dashkit_kiboui/",
    project_urls={
        "Homepage": "https://pypi.org/project/dashkit_kiboui/",
        "Source": "https://github.com/iamgp/dash_dashkit",
        "Issues": "https://github.com/iamgp/dash_dashkit/issues",
    },
    packages=["dashkit_kiboui"],
    include_package_data=True,
    package_data={
        "dashkit_kiboui": [
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
