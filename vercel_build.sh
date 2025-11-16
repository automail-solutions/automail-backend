#!/bin/bash
set -e

# Install Python dependencies
python -m pip install -r requirements.txt

# Create __pycache__ directory if it doesn't exist
python -m mkdir -p __pycache__
