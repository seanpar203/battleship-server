from wta_app.host.models import HostName
from wta_app.tests.test_base import BaseTestCase
from wta_app.tests.test_data import TEST_DATA, create_test_data
from wta_app.time_spent.models import TimeSpent
from wta_app.user.models import UserToken, db


class UserModelTests(BaseTestCase):
	"""UserToken Unit Tests """
	token = TEST_DATA['user']
	time = TEST_DATA['time']
	host = TEST_DATA['host']

	def test_can_create_user(self):
		""" Tests that a User is actually created. """
		user = create_test_data(data=self.token, model=UserToken, retrn=True)

		# Verify user is in db.
		assert user in db.session

	def test_correct_token(self):
		""" Tests that the token is the same as the one passed in. """
		user = create_test_data(data=self.token, model=UserToken, retrn=True)

		# Verify user has correct token.
		assert user.token == self.token

	def test_time_spent_relationship(self):
		""" Tests that a one-to-many relationship exists with TimeSpent. """
		user = UserToken(self.token)
		time = TimeSpent(self.time)

		# Make Relationship
		user.time_spent.append(time)

		# Add & Save
		db.session.add(user)
		db.session.add(time)
		db.session.commit()

		# Verify one-to-many relationship
		assert user.time_spent.count() == 1

	def test_host_access_through_time_spent(self):
		""" Tests accessing HostName host attribute from User object
		through TimeSpent Object.
		"""
		user = UserToken(self.token)
		time = TimeSpent(self.time)
		host = HostName(self.host)

		# Make Relationship
		user.time_spent.append(time)
		time.host.append(host)

		# Add & Save
		db.session.add(user)
		db.session.add(time)
		db.session.add(host)
		db.session.commit()

		# Verify accessing host through TimeSpent relationship.
		assert user.time_spent.first().host.first().host == self.host
