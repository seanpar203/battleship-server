from wta_app import db


def add_then_commit(*args):
	""" Adds arbitrary amount and saves to db

	Args:
		*args: Value of objects to add & save.
	"""
	for arg in args:
		db.session.add(arg)
	db.session.commit()


def results_to_dict(results):
	""" Generates informative dicts from tuples.

	Args:
		results: Value of tuples.

	Returns:
		dict: Value of formatted tuples.
	"""
	for i, (k, v) in enumerate(results):
		yield {k: int(v)}
