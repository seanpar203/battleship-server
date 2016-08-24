# -*- coding: utf-8 -*-
""" Web Time Analytics Models.

This module defines the Models and their relationships.
"""
from app import db


class User(db.Model):
	""" Basic user class that stores unique tokens. """

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	token = db.Column(db.String(), unique=True)

	# Built-in Override Methods.
	def __init__(self, token):
		""" Creates new User.

		Args:
			token (str): A uuid string.
		"""
		self.token = token

	def __repr__(self):
		""" Returns simple object representation.

		Returns:
			str: String representation of User Object.
		"""
		return '<User id:{0}>'.format(self.id)


class TimeSpent(db.Model):
	""" Model for storing Users time spent(host, minutes) """

	# Attributes
	id = db.Column(db.Integer, primary_key=True)
	minutes = db.Column(db.BigInteger)
	host = db.Column(db.String())

	# Relations
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship(
		'User', backref=db.backref('time_spent', lazy='dynamic')
	)

	# Built-in Override Methods.
	def __init__(self, minutes, host, user):
		""" Creates TimeSpent Object with relationship to User.

		Args:
			minutes (int): Value of time spent on web page.
			host (str): Value of host name of web page.
			user (object): User who was on web page.
		"""
		self.minutes = minutes
		self.host = host
		self.user = user

	def __repr__(self):
		""" Returns simple object representation.

		Returns:
			str: String representation of TimeSpent Object.
		"""
		return '<TimeSpent host:{0}>'.format(self.host)
