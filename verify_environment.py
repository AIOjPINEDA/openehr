#!/usr/bin/env python
"""
OpenEHR Bootcamp Environment Verification Script
==============================================

PURPOSE:
This script checks if your development environment is correctly set up for the OpenEHR Bootcamp.
It verifies that all required software, packages, and configurations are in place.

USAGE:
    python verify_environment.py

WHAT THIS SCRIPT CHECKS:
1. Python version - Ensures you have Python 3.8 or higher
2. Conda environment - Verifies if you're running in the correct Conda environment
3. Node.js and npm - Checks if these are installed and their versions
4. Required Python packages - Verifies all packages from environment.yml are installed
5. Environment variables - Checks if the .env file exists with required variables

OUTPUT:
The script provides color-coded output with checkmarks (✅), warnings (⚠️), and errors (❌)
to help you identify what's correctly configured and what needs attention.

TROUBLESHOOTING:
If you see warnings or errors:
- For missing packages: Run 'conda env update -f environment.yml'
- For missing .env file: Copy .env.example to .env and configure it
- For version issues: Update the software to the recommended version

AUTHOR:
Created for the OpenEHR Bootcamp
"""

import platform
import subprocess
import importlib.util
import os
import sys
from pathlib import Path

# ANSI color codes for terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_success(message):
    """Print a success message with a green checkmark."""
    print(f"{GREEN}✅ {message}{RESET}")

def print_warning(message):
    """Print a warning message with a yellow warning sign."""
    print(f"{YELLOW}⚠️ {message}{RESET}")

def print_error(message):
    """Print an error message with a red X."""
    print(f"{RED}❌ {message}{RESET}")

def print_section(title):
    """Print a section title."""
    print(f"\n{BOLD}{title}{RESET}")

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    print_section("Checking Python Version")

    version = platform.python_version()
    major, minor, _ = map(int, version.split('.'))

    if major >= 3 and minor >= 8:
        print_success(f"Python version {version} (recommended: 3.8+)")
    else:
        print_error(f"Python version {version} (recommended: 3.8+)")

def check_conda_environment():
    """Check if running in the correct conda environment."""
    print_section("Checking Conda Environment")

    env_name = os.environ.get('CONDA_DEFAULT_ENV')
    if env_name in ['openehr-bootcamp', 'openehr-env']:
        print_success(f"Running in conda environment: {env_name}")
    elif env_name:
        print_warning(f"Running in conda environment: {env_name} (expected: openehr-bootcamp or openehr-env)")
    else:
        print_error("Not running in a conda environment")

def check_node_npm():
    """Check if Node.js and npm are installed and their versions."""
    print_section("Checking Node.js and npm")

    # Check Node.js
    try:
        node_version = subprocess.check_output(["node", "--version"], text=True).strip()
        if node_version.startswith("v18"):
            print_success(f"Node.js version: {node_version} (recommended: v18)")
        else:
            print_warning(f"Node.js version: {node_version} (recommended: v18)")
    except (subprocess.SubprocessError, FileNotFoundError):
        print_error("Node.js not found. Please install Node.js v18")

    # Check npm
    try:
        npm_version = subprocess.check_output(["npm", "--version"], text=True).strip()
        print_success(f"npm version: {npm_version}")
    except (subprocess.SubprocessError, FileNotFoundError):
        print_error("npm not found. Please install npm")

def check_python_packages():
    """Check if required Python packages are installed."""
    print_section("Checking Required Python Packages")

    required_packages = [
        "python-dotenv",
        "httpx",
        "pytest",
        "fastapi",
        "uvicorn",
        "jinja2",
        "pydantic",
        "streamlit",
        "dash",
        "dash-bootstrap-components",
        "lxml",
        "black",
        "flake8",
        "isort",
        "tqdm",
        "rich"
    ]

    for package in required_packages:
        package_name = package.replace("-", "_")
        try:
            __import__(package_name)
            print_success(f"Package installed: {package}")
        except ImportError:
            try:
                # Some packages have different import names
                if package == "python-dotenv":
                    __import__("dotenv")
                    print_success(f"Package installed: {package}")
                else:
                    print_error(f"Package not installed: {package}")
            except ImportError:
                print_error(f"Package not installed: {package}")

def check_env_file():
    """Check if .env file exists and contains required variables."""
    print_section("Checking Environment Variables")

    env_file = Path(".env")
    env_example = Path(".env.example")

    if env_file.exists():
        print_success(".env file exists")

        # Check if .env file has required variables
        required_vars = ["EHRBASE_URL", "EHRBASE_USERNAME", "EHRBASE_PASSWORD"]
        with open(env_file, "r") as f:
            env_content = f.read()

        for var in required_vars:
            if var in env_content:
                print_success(f"Environment variable found: {var}")
            else:
                print_warning(f"Environment variable missing: {var}")
    else:
        print_warning(".env file not found. Please copy .env.example to .env and configure it")

        if env_example.exists():
            print_success(".env.example file exists and can be used as a template")
        else:
            print_error(".env.example file not found")

def main():
    """Run all environment checks."""
    print(f"{BOLD}OpenEHR Bootcamp Environment Verification{RESET}")
    print("=" * 50)

    check_python_version()
    check_conda_environment()
    check_node_npm()
    check_python_packages()
    check_env_file()

    print("\n" + "=" * 50)
    print(f"{BOLD}Verification Complete{RESET}")

if __name__ == "__main__":
    main()
