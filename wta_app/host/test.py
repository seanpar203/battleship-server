from app import db
from tests.test_base import BaseTestCase
from tests.test_data import TEST_DATA, create_test_data
from host.models import HostName


class HostModelTests(BaseTestCase):
	"""HostName Unit Tests """
	token = TEST_DATA['user']
	time = TEST_DATA['time']
	host = TEST_DATA['host']

	def test_can_host_name(self):
		""" Tests that a User is actually created. """
		host_name = create_test_data(data=self.host, model=HostName, retrn=True)

		# Verify host is in db.
		assert host_name in db.session

	def test_correct_host_name(self):
		""" Tests that the token is the same as the one passed in. """
		host_name = create_test_data(data=self.host, model=HostName, retrn=True)

		# Verify host has correct token.
		assert host_name.host == self.host
