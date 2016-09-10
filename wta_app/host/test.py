from wta_app import db
from wta_app.models import Host
from wta_app.tests.test_base import BaseTestCase
from wta_app.tests.test_data import TEST_DATA, create_test_data


class HostModelTests(BaseTestCase):
	"""Host Unit Tests """
	token = TEST_DATA['account']
	time = TEST_DATA['time']
	host = TEST_DATA['host']

	def test_can_host_name(self):
		""" Tests that a Host is actually created. """
		host_name = create_test_data(
				data=self.host,
				model=Host,
				retrn=True
		)

		# Verify host is in db.
		assert host_name in db.session

	def test_correct_host_name(self):
		""" Tests that the token is the same as the one passed in. """
		host_name = create_test_data(data=self.host, model=Host,
		                             retrn=True)

		# Verify host has correct token.
		assert host_name.host == self.host
