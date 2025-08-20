import json
from pathlib import Path

from setuptools import setup

# Read metadata from package-info.json
package_json = json.loads(
    (Path(__file__).parent / "dashkit_shadcn" / "package-info.json").read_text()
)

setup(
    name="dashkit_shadcn",
    version="1.0.0",
    description="shadcn/ui Chart components for Dash with native theming support",
    packages=["dashkit_shadcn"],
    include_package_data=True,
    package_data={
        "dashkit_shadcn": [
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
    author="Dashkit Team",
    license="MIT",
)