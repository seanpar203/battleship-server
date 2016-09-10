from wta_app import db
from wta_app.models import Host, Time
from wta_app.tests.test_base import BaseTestCase
from wta_app.tests.test_data import TEST_DATA, create_test_data


class TimeModelTests(BaseTestCase):
	"""Time Unit Tests """
	seconds = TEST_DATA['time']
	host = TEST_DATA['host']

	def test_can_create_time(self):
		""" Tests that a Time is actually created. """
		time = create_test_data(
				data=self.seconds,
				model=Time,
				retrn=True
		)

		# Verify user is in db.
		assert time in db.session

	def test_correct_time(self):
		""" Tests that the seconds is the same as the one passed in. """
		time = create_test_data(
				data=self.seconds,
				model=Time,
				retrn=True
		)

		# Verify user has correct token.
		assert time.seconds == self.seconds

	def test_host_relationship(self):
		""" Tests that a one-to-many relationship exists with Host. """
		time = Time(self.seconds)
		host = Host(self.host)

		# Make Relationship
		time.host.append(host)

		# Add & Save
		db.session.add(time)
		db.session.add(host)
		db.session.commit()

		# Verify one-to-many relationship
		assert time.host.count() == 1

	def test_host_name_access(self):
		""" Tests that a Time object has access to Host host
		attribute. """
		time = Time(self.seconds)
		host = Host(self.host)

		# Make Relationship
		time.host.append(host)

		# Add & Save
		db.session.add(time)
		db.session.add(host)
		db.session.commit()

		# Verify access to HotName host attribute.
		assert time.host.first().host == self.host
