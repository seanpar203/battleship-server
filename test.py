""" Testing for Web Time Analytics app.

This module, replicates & tests the functionality of the
flask server and it's routes.
"""

import unittest

from flask_testing import TestCase

from app import app, db, User, TimeSpent
from config import TestConfig


class MyTestCase(TestCase):
	SQLALCHEMY_DATABASE_URI = "sqlite://"

	def create_app(self):
		app.config.from_object(TestConfig)
		return app(self)

	def setUp(self):
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()


if __name__ == '__main__':
	unittest.main()
