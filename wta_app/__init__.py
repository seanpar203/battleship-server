import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config
app = Flask(__name__)
app_settings = os.getenv('APP_SETTINGS', 'wta_app.config.DevConfig')
app.config.from_object(app_settings)

# DB Connection
db = SQLAlchemy(app)

# Blueprints
from wta_app.user.views import users
app.register_blueprint(users)
