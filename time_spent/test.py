from app import db
from tests.test_base import BaseTestCase
from tests.test_data import TEST_DATA, create_test_data
from time_spent.models import TimeSpent
from host.models import HostName


class UserModelTests(BaseTestCase):
	"""User Unit Tests """
	minutes = TEST_DATA['time']
	host = TEST_DATA['host']

	def test_can_create_time(self):
		""" Tests that a TimeSpent is actually created. """
		time = create_test_data(data=self.minutes, model=TimeSpent, retrn=True)

		# Verify user is in db.
		assert time in db.session

	def test_correct_time(self):
		""" Tests that the minutes is the same as the one passed in. """
		time = create_test_data(data=self.minutes, model=TimeSpent, retrn=True)

		# Verify user has correct token.
		assert time.minutes == self.minutes

	def test_host_relationship(self):
		""" Tests that a one-to-many relationship exists with HostName. """
		time = TimeSpent(self.minutes)
		host = HostName(self.host)

		# Make Relationship
		time.host.append(host)

		# Add & Save
		db.session.add(time)
		db.session.add(host)
		db.session.commit()

		# Verify one-to-many relationship
		assert time.host.count() == 1
