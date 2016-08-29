""" Time Spent Model

This module represents the attributes of time spent on
the web. Creating a one-to-one relationship with a Host
Object on instantiation as a reference to exactly where the
time was spent.

"""

from app import db


class TimeSpent(db.Model):
	""" Model for storing Users time spent(host, minutes) """

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	minutes = db.Column(db.BigInteger)

	# Relations
	user_id = db.Column(db.Integer, db.ForeignKey('user_token.id'))
	host = db.relationship('HostName', backref='time_spent', lazy='dynamic')

	# Built-in Override Methods.
	def __init__(self, minutes):
		""" Creates new TimeSpent with amount of minutes.

		Notes:
			This model has a many-to-one relationship with the
			UserToken model and a one-to-many relationship with the
			HostName model.

		Args:
			minutes (int): Value of time spent on active web page.
		"""
		self.minutes = minutes

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of TimeSpent Object.
		"""
		return '<TimeSpent {}>'.format(self.minutes)
