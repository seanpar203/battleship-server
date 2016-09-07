from wta_app import db


def add_then_commit(*args):
	""" Adds arbitrary amount and saves to db

	Args:
		*args: Value of objects to add & save.
	"""
	for arg in args:
		db.session.add(arg)
	db.session.commit()


def unique_host_names(times):
	for time in times:
		yield time.host.first().host_name
