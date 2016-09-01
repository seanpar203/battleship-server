""" Testing for Web Time Analytics app.

This is the base test class which will be extended to
run more specific tests against different roles of the
backend.
"""

from flask_testing import TestCase

from wta_app import create_app
from wta_app.user.models import db


class BaseTestCase(TestCase):
    """ Testing for flask routes """

    def create_app(self):
        app = create_app()
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
