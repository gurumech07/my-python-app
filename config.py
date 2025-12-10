import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instance"
INSTANCE_DIR.mkdir(exist_ok=True)

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

SQLALCHEMY_DATABASE_URI = (
    os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{INSTANCE_DIR / 'todo.db'}",
    )
)
SQLALCHEMY_TRACK_MODIFICATIONS = False