""" Testing for Web Time Analytics app.

This is the base test class which will be extended to
run more specific tests against different roles of the
backend.
"""

from flask_testing import TestCase

from app import app, db


class BaseTestCase(TestCase):
    """ Testing for flask routes """

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
