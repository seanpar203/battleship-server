from wta_app import db
from datetime import date


class Account(db.Model):
	""" Basic Account class that stores unique tokens. """

	__tablename__ = 'account'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	token = db.Column(db.String(), unique=True)
	time_spent = db.relationship('Time', backref='user', lazy='dynamic')

	# Built-in Override Methods.
	def __init__(self, token):
		""" Creates new Account.

		Notes:
			This model has a one-to many relationship with the
			Time model.

		Args:
			token (str): A uuid string.
		"""
		self.token = token

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of Account Object.
		"""
		return '<Account {}>'.format(self.id)

	@classmethod
	def get_or_create(cls, token):
		user = cls.query.filter_by(token=token).first()
		if user is not None:
			return user
		else:
			instance = cls(token)
			return instance


""" Many to Many Table for Host & Time. """
host_times = db.Table(
		'host_time',
		db.Column('time_id', db.Integer, db.ForeignKey('time.id')),
		db.Column('host_id', db.Integer, db.ForeignKey('host.id'))
)


class Time(db.Model):
	""" Model for storing Accounts time spent(host, seconds) """

	__tablename__ = 'time'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	day = db.Column(db.Date)
	seconds = db.Column(db.BigInteger)

	# Relations
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
	host = db.relationship(
			'Host',
			secondary=host_times,
			backref='time_spent',
			lazy='dynamic'
	)

	# Built-in Override Methods.
	def __init__(self, seconds):
		""" Creates new Time with amount of seconds.

		Notes:
			This model has a many-to-one relationship with the
			Account model and a one-to-many relationship with the
			Host model.

		Args:
			seconds (int): Value of time spent on active web page.
		"""
		self.seconds = seconds
		self.day = date.isoformat(date.today())

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of Time Object.
		"""
		return '<Time {}>'.format(self.seconds)


class Host(db.Model):
	""" Model for storing User's active tab host name. """

	__tablename__ = 'host'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	host_name = db.Column(db.String(), unique=True)

	# Built-in Overrides
	def __init__(self, host_name):
		""" Create new instance of Host class.

		Notes:
			This model has a one-to-many relationship with the
			Time model. Using unique strings allow to reduce
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
		return '<Host {}>'.format(self.host_name)

	@classmethod
	def get_or_create(cls, host_name):
		host = cls.query.filter_by(host_name=host_name).first()
		if host is not None:
			return host
		else:
			instance = cls(host_name)
			return instance