from wta_app import db
from wta_app.models import Account, Time, Host
from wta_app.tests.test_base import BaseTestCase
from wta_app.tests.test_data import TEST_DATA, create_test_data


class AccountModelTests(BaseTestCase):
	"""Account Unit Tests """
	token = TEST_DATA['account']
	time = TEST_DATA['time']
	host = TEST_DATA['host']

	def test_can_create_account(self):
		""" Tests that a Account is actually created. """
		account = create_test_data(data=self.token, model=Account, retrn=True)

		# Verify account is in db.
		assert account in db.session

	def test_correct_token(self):
		""" Tests that the token is the same as the one passed in. """
		account = create_test_data(data=self.token, model=Account, retrn=True)

		# Verify account has correct token.
		assert account.token == self.token

	def test_time_spent_relationship(self):
		""" Tests that a one-to-many relationship exists with Time. """
		account = Account(self.token)
		time = Time(self.time)

		# Make Relationship
		account.time_spent.append(time)

		# Add & Save
		db.session.add(account)
		db.session.add(time)
		db.session.commit()

		# Verify one-to-many relationship
		assert account.time_spent.count() == 1

	def test_host_access_through_time_spent(self):
		""" Tests accessing Host host attribute from Account object
		through Time Object.
		"""
		account = Account(self.token)
		time = Time(self.time)
		host = Host(self.host)

		# Make Relationship
		account.time_spent.append(time)
		time.host.append(host)

		# Add & Save
		db.session.add(account)
		db.session.add(time)
		db.session.add(host)
		db.session.commit()

		# Verify accessing host through Time relationship.
		assert account.time_spent.first().host.first().host == self.host
