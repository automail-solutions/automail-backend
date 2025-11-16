import sys
from pathlib import Path

# Add the current directory to the Python path
sys.path.append(str(Path(__file__).parent))

# Import the app from src.main
from src.main import app

# For Vercel deployment
handler = app