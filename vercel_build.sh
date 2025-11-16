#!/bin/bash
set -e

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Install the package in development mode
python -m pip install -e .

# Create necessary directories
mkdir -p __pycache__

# Create a .python-version file for Vercel
echo "3.12.3" > .python-version
