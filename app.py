""" Module that handles all the routes for the web-time-analytics extension."""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from user.views import users

# Flask Config.
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create DB Connection.
db = SQLAlchemy(app)

# Register blueprints.
app.register_blueprint(users)

# Import Models
from user.models import UserToken
from host.models import HostName
from time_spent.models import TimeSpent


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
