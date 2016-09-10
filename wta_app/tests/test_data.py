""" Test Data & Methods.

This module represents the test data and methods to be
used in python packages test.py,
"""
from wta_app import db

TEST_USER_TOKEN = '123456'
TEST_TIME_SPENT = 10
TEST_HOST_NAME = 'facebook.com'
TEST_DATA = {
	'time':    TEST_TIME_SPENT,
	'host':    TEST_HOST_NAME,
	'account': TEST_USER_TOKEN,
}


def create_test_data(**kwargs):
	""" Runs dynamic test based on passed in kwargs.

	Notes:
		The intention of this function is to be able to run
		generic tests and pass in the data, model & a bool if
		a return value is desired for further testing.

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
