from sqlalchemy.dialects.postgresql import ARRAY

from battleship import db


class Account(db.Model):
	""" Account class that stores unique emails. """

	__tablename__ = 'account'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(), unique=True)

	# Relationships
	games = db.relationship(
		'Game',
		lazy='dynamic',
		backref='account',
		cascade="all, delete-orphan"
	)

	# Built-in Override Methods.
	def __init__(self, user_name):
		""" Creates new Account.

		Args:
			user_name (str): A unique user name.
		"""
		self.user_name = user_name

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of Account Object.
		"""
		return '<Account {}>'.format(self.user_name)

	@classmethod
	def get_or_create(cls, user_name):
		account = cls.query.filter_by(user_name=user_name).first()
		if account is not None:
			return account
		else:
			instance = cls(user_name)
			return instance


class Game(db.Model):
	""" Game model for storing unique game. """

	__tablename__ = 'game'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	won = db.Column(db.BOOLEAN, default=False)

	# Relationships
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
	# Relationships
	board = db.relationship(
		'Board',
		uselist=False,
		lazy='select',
		backref='game',
		cascade="all, delete-orphan"
	)

	# Built-in Override Methods.
	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of Game Object.
		"""
		return '<Game {}>'.format(self.id)


class Board(db.Model):
	""" Board model for storing unique Board. """

	__tablename__ = 'board'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)

	# Relationships
	game_id = db.Column(db.Integer, db.ForeignKey('game.id'))

	# Relationships
	coords = db.relationship(
		'Coords',
		uselist=False,
		lazy='select',
		backref='board',
		cascade="all, delete-orphan"
	)

	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of Board Object.
		"""
		return '<Board {}>'.format(self.id)

	@classmethod
	def get_or_create(cls, game):
		board = cls.query.filter_by(game_id=game.id).first()
		if board is not None:
			return board
		else:
			instance = cls()
			game.board = instance
			return instance


class Coords(db.Model):
	""" Coords model for storing unique coordinates for a single Board. """

	__tablename__ = 'coord'

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	cpu_coords = db.Column(ARRAY(db.Integer))
	acc_coords = db.Column(ARRAY(db.Integer))

	# Relationships
	board_id = db.Column(db.Integer, db.ForeignKey('board.id'))

	# Built-in Override Methods.
	def __str__(self):
		""" Returns Object string representation.

		Returns:
			str: String representation of Coords Object.
		"""
		return '<Coords {}>'.format(self.id)

	# Methods
	def add_coords(self, attr, coords):
		setattr(self, attr, coords)

	@classmethod
	def get_or_create(cls, board):
		coords = cls.query.filter_by(board_id=board.id).first()
		if coords is not None:
			return coords
		else:
			instance = cls()
			board.coords = instance
			return instance
