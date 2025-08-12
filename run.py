#!/usr/bin/env python3
"""Simple runner script for the Dashkit-style Dash app."""

import subprocess
import sys
from pathlib import Path


def main():
    """Run the Dash application."""
    app_path = Path(__file__).parent / "src" / "dashkit_demo" / "app.py"

    try:
        subprocess.run([sys.executable, str(app_path)], check=True)
    except KeyboardInterrupt:
        print("\nShutting down...")
    except subprocess.CalledProcessError as e:
        print(f"Error running app: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
