""" Web Time Analytics Migrations Manager.

This module defines this projects migration manager.
"""
import os

from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

from app import app, db

# Load Current Config Settings.
app.config.from_object(os.environ['APP_SETTINGS'])

# Create Instances.
migrate = Migrate(app, db)
manager = Manager(app)

# Add method to manager.
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
