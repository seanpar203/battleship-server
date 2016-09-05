from wta_app import db


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

	@classmethod
	def get_or_create(cls, token):
		user = cls.query.filter_by(token=token).first()
		if user is not None:
			return user
		else:
			instance = cls(token=token)
			db.session.add(instance)
			db.session.commit()
			return instance


class TimeSpent(db.Model):
	""" Model for storing Users time spent(host, minutes) """

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	seconds = db.Column(db.BigInteger)

	# Relations
	user_id = db.Column(db.Integer, db.ForeignKey('user_token.id'))
	host = db.relationship('HostName', backref='time_spent', lazy='dynamic')

	# Built-in Override Methods.
	def __init__(self, seconds):
		""" Creates new TimeSpent with amount of minutes.

		Notes:
			This model has a many-to-one relationship with the
			UserToken model and a one-to-many relationship with the
			HostName model.

		Args:
			seconds (int): Value of time spent on active web page.
		"""
		self.seconds = seconds

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of TimeSpent Object.
		"""
		return '<TimeSpent {}>'.format(self.minutes)


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

	@classmethod
	def get_or_create(cls, host):
		host = cls.query.filter_by(host=host).first()
		if host is not None:
			return host
		else:
			instance = cls(host=host)
			db.session.add(instance)
			db.session.commit()
			return instance
