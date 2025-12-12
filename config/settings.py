import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/data/prices.sqlite")
USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0")

SQLITE_CONNECT_ARGS = {"check_same_thread": False}
