""" Web Time Analytics Migrations Manager.

This module defines this projects migration manager.
"""
import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from wta_app.app import app, db

# Set Current Environment Settings.
app.config.from_object(os.environ['APP_SETTINGS'])

# Create Instances.
migrate = Migrate(app, db)
manager = Manager(app)

# Add method.
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
