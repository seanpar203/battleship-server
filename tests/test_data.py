""" Test Data & Methods.

This module represents the test data and methods to be
used in python packages test.py,
"""
from app import db

TEST_USER_TOKEN = '123456'
TEST_TIME_SPENT = 10
TEST_HOST_NAME = 'facebook.com'
TEST_DATA = {
	'user': TEST_USER_TOKEN,
	'time': TEST_TIME_SPENT,
	'host': TEST_HOST_NAME
}


def create_test_data(**kwargs):
	""" Runs dynamic test based on passed in kwargs.

	Notes:
		The intention of this function is to be able to run
		generic tests and pass in the data, model & a bool if
		a return value is desired for further testing.

	Args:
		**kwargs: Value of data, model & return bool.

	Keyword Args:
		data (str|int): Value of the data to use with creating model.
		model (object): Model to be created with data.
		retrn (bool): True to return the new object. Defaults to False.


	Examples:

		from app import db
		from user.models import UserToken
		from tests.test_data import create_dummy_data, DUMMY_TEST_DATA

		user = create_dummy_data(DUMMY_TEST_DATA['user'], UserToken, True)



	Returns:
		object: Value of newly created & inserted model.

	"""
	data = kwargs['data']
	model = kwargs['model']
	retrn = kwargs.get('retrn', False)
	test = model(data)
	db.session.add(test)
	db.session.commit()
	if retrn:
		return test
