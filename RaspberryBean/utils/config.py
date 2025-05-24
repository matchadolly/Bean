"""
🎀🎀
Load environment variables on first import.
🎀🎀
"""
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path.home() / "Bean" / "RaspberryBean"
load_dotenv(PROJECT_ROOT / ".env")
