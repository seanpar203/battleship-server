""" Web Time Analytics Migrations Manager.

This module defines this projects migration manager.
"""
import os
import unittest
import coverage

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

COV = coverage.coverage(
		branch=True,
		include='wta_app/*',
		omit=[
			'wta_app/tests/*',
			'wta_app/config.py',
			'wta_app/*/__init__.py'
		]
)

COV.start()

from wta_app import app, db
from wta_app.models import UserToken, HostName, TimeSpent

# Create Instances.
migrate = Migrate(app, db)
manager = Manager(app)

# Add method.
manager.add_command('db', MigrateCommand)


@manager.command
def test():
	"""Runs the unit tests without test coverage."""
	tests = unittest.TestLoader().discover('wta_app/', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	return 1


@manager.command
def cov():
	"""Runs the unit tests with coverage."""
	tests = unittest.TestLoader().discover('wta_app/', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		COV.stop()
		COV.save()
		print('Coverage Summary:')
		COV.report()
		basedir = os.path.abspath(os.path.dirname(__file__))
		covdir = os.path.join(basedir, 'tmp/coverage')
		COV.html_report(directory=covdir)
		print('HTML version: file://%s/index.html' % covdir)
		COV.erase()
		return 0
	return 1


@manager.command
def create_db():
	"""Creates the db tables."""
	db.create_all()


@manager.command
def drop_db():
	"""Drops the db tables."""
	db.drop_all()


if __name__ == '__main__':
	manager.run()
