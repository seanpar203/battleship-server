from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class HostName(db.Model):
	""" Model for storing User's active tab host name. """

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	host = db.Column(db.String(), unique=True)

	# Relations
	time_spent_id = db.Column(db.Integer, db.ForeignKey('time_spent.id'))

	# Built-in Overrides
	def __init__(self, host):
		""" Create new instance of Host class.

		Notes:
			This model has a one-to-many relationship with the
			TimeSpent model. Using unique strings allow to reduce
			the amount of new rows every time a request comes in to
			only unique host names.


		Examples:
			The value of a host name would be:
			facebook.com,
			linkedin.com,
			reddit.com

		Args:
			host (str): Value of the active tab host name.
		"""
		self.host = host

	def __str__(self):
		""" Returns Object string representation. """
		return '<Host {}>'.format(self.host)
