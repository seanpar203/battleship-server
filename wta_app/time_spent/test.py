from wta_app import db
from wta_app.models import HostName, TimeSpent
from wta_app.tests.test_base import BaseTestCase
from wta_app.tests.test_data import TEST_DATA, create_test_data


class TimeModelTests(BaseTestCase):
	"""TimeSpent Unit Tests """
	minutes = TEST_DATA['time']
	host = TEST_DATA['host']

	def test_can_create_time(self):
		""" Tests that a TimeSpent is actually created. """
		time = create_test_data(
				data=self.minutes,
				model=TimeSpent,
				retrn=True
		)

		# Verify user is in db.
		assert time in db.session

	def test_correct_time(self):
		""" Tests that the minutes is the same as the one passed in. """
		time = create_test_data(
				data=self.minutes,
				model=TimeSpent,
				retrn=True
		)

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

	def test_host_name_access(self):
		""" Tests that a TimeSpent object has access to HostName host
		attribute. """
		time = TimeSpent(self.minutes)
		host = HostName(self.host)

		# Make Relationship
		time.host.append(host)

		# Add & Save
		db.session.add(time)
		db.session.add(host)
		db.session.commit()

		# Verify access to HotName host attribute.
		assert time.host.first().host == self.host
