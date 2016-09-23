from battleship import db

CREATED = 201
OK_REQUEST = 200
BAD_REQUEST = 400
UNAUTHORIZED = 401


def add_then_commit(*args):
	""" Adds arbitrary amount and saves to db

	Args:
		*args: Value of objects to add & save.
	"""
	for arg in args:
		db.session.add(arg)
	db.session.commit()
