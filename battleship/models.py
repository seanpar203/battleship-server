from battleship import db
from sqlalchemy import Integer
from sqlalchemy.dialects import postgresql


class Account(db.Model):
	""" Account class that stores unique emails. """

	__tablename__ = 'account'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(), unique=True)

	# Relationships
	games = db.relationship(
			'Game',
			lazy='dynamic',
			backref='account',
			cascade="all, delete-orphan"
	)

	# Built-in Override Methods.
	def __init__(self, email):
		""" Creates new Account.

		Args:
			email (str): A email address.
		"""
		self.email = email

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of Account Object.
		"""
		return '<Account {}>'.format(self.email)

	@classmethod
	def get_or_create(cls, email):
		user = cls.query.filter_by(email=email).first()
		if user is not None:
			return user
		else:
			instance = cls(email)
			return instance


class Game(db.Model):
	""" Game model for storing unique game. """

	__tablename__ = 'game'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	won = db.Column(db.BOOLEAN, default=0)

	# Relationships
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

	# Built-in Override Methods.
	def __init__(self, account):
		""" Creates new Game.

		Args:
			account (str): A account model.
		"""
		self.account_id = account

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of Game Object.
		"""
		return '<Game {}>'.format(self.id)


class Board(db.Model):
	""" Game model for storing unique game. """

	__tablename__ = 'board'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)

	# Relationships
	game_id = db.Column(db.Integer, db.ForeignKey('game.id'))

	# Relationships
	positions = db.relationship(
			'Position',
			lazy='dynamic',
			backref='board',
			cascade="all, delete-orphan"
	)

	# Built-in Override Methods.
	def __init__(self, game):
		""" Creates new Board.

		Args:
			game (str): A Game model.
		"""
		self.game_id = game

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of Board Object.
		"""
		return '<Board {}>'.format(self.id)


class Position(db.Model):
	""" Position model for storing positions. """

	__tablename__ = 'Position'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	cpu_positions = db.Column(postgresql.ARRAY(Integer))
	acc_positions = db.Column(postgresql.ARRAY(Integer))

	# Built-in Override Methods.
	def __init__(self, position):
		""" Creates new Position.

		Args:
			position (int): A integer of position.
		"""
		self.position = position

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of Position Object.
		"""
		return '<Position {}>'.format(self.position)
