import sys
import os
from pathlib import Path

# Add the backend directory to sys.path so modules can be imported
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / "Backend" / "biosync-net-backend" / "biosync-net-backend"
sys.path.append(str(BACKEND_DIR))

# Import the FastAPI app
from main import app

# Vercel requires the variable to be named 'app'
# Since we imported 'app' from main, it's already there.
