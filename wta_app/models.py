from wta_app import db
from datetime import date


class UserToken(db.Model):
	""" Basic token class that stores unique tokens. """

	__tablename__ = 'user'

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
			instance = cls(token)
			return instance


time_hosts = db.Table(
		'time_hosts',
		db.Column('time_id', db.Integer, db.ForeignKey('time.time_id')),
		db.Column('host_id', db.Integer, db.ForeignKey('host.host_id'))
)


class TimeSpent(db.Model):
	""" Model for storing Users time spent(host, minutes) """

	__tablename__ = 'time'

	# Attributes
	day = db.Column(db.Date)
	time_id = db.Column(db.Integer, primary_key=True)
	seconds = db.Column(db.BigInteger)

	# Relations
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	host = db.relationship(
			'HostName',
			secondary=time_hosts,
			backref='time_spent',
			lazy='dynamic'
	)

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
		self.day = date.isoformat(date.today())

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of TimeSpent Object.
		"""
		return '<TimeSpent {}>'.format(self.minutes)


class HostName(db.Model):
	""" Model for storing User's active tab host name. """

	__tablename__ = 'host'

	# Attributes
	host_id = db.Column(db.Integer, primary_key=True)
	host_name = db.Column(db.String(), unique=True)

	# Built-in Overrides
	def __init__(self, host_name):
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
			host_name (str): Value of the active tab host name.
		"""
		self.host_name = host_name

	def __str__(self):
		""" Returns Object string representation. """
		return '<Host {}>'.format(self.host)

	@classmethod
	def get_or_create(cls, host_name):
		host = cls.query.filter_by(host_name=host_name).first()
		if host is not None:
			return host
		else:
			instance = cls(host_name)
			return instance
