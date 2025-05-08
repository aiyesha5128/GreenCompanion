import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy with the Base
db = SQLAlchemy(model_class=Base)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

# Configure the database connection

# database_url = os.environ.get("DATABASE_URL", "").replace("\\x3a", ":")
# app.config["SQLALCHEMY_DATABASE_URI"] = database_url
from pathlib import Path

# Get the absolute path to the database file in the instance directory
db_path = Path(__file__).resolve().parent / 'instance' / 'plantpal.db'

# Update the database URI to the absolute path
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

print("Database URL:", app.config["SQLALCHEMY_DATABASE_URI"])


app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the app with the extension
db.init_app(app)

with app.app_context():
    # Import models to ensure tables are created
    import models  # noqa: F401
    db.create_all()
