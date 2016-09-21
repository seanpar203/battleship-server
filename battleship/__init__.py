import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Config
app = Flask(__name__)

CORS(app)
app_settings = os.getenv('APP_SETTINGS', 'battleship.config.DevConfig')
app.config.from_object(app_settings)

# DB Connection
db = SQLAlchemy(app)