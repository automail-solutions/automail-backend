import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent / "src"))

from main import app  # This now imports from src/main.py

# For Vercel deployment
handler = app