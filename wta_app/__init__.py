import os

from flask import Flask

from wta_app.host.models import HostName
from wta_app.time_spent.models import TimeSpent
from wta_app.user.models import UserToken


def create_app():
	app = Flask(__name__)
	app.config.from_object(os.environ['APP_SETTINGS'])
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	# Create DB Connection.
	from wta_app.user.models import db
	db.init_app(app)

	# Register blueprints.
	from wta_app.user.views import users
	app.register_blueprint(users)

	return app
