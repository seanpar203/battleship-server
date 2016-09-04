import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wta_app.user.views import users

# Config
app = Flask(__name__)
app_settings = os.getenv('APP_SETTINGS', 'wta_app.config.DevConfig')
app.config.from_object(app_settings)

# DB Connection
db = SQLAlchemy(app)

# Blueprints
app.register_blueprint(users)
