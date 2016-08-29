from app import db


class UserToken(db.Model):
	""" Basic token class that stores unique tokens. """

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	token = db.Column(db.String(), unique=True)
	time_spent = db.relationship('TimeSpent', backref='user', lazy='dynamic')

	# Built-in Override Methods.
	def __init__(self, token):
		""" Creates new User.

		Notes:
			This model has a one-to many relationship with the
			TimeSpent model.

		Args:
			token (str): A uuid string.
		"""
		self.token = token

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of User Object.
		"""
		return '<User {}>'.format(self.id)
