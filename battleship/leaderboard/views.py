from flask import Blueprint, jsonify, request
from sqlalchemy import func
from flask_cors import cross_origin
from battleship import db

from battleship.helpers import OK_REQUEST
from battleship.models import Account, Coords, Game

# Create new flask blueprint
board = Blueprint('board', __name__)


@board.route('/leaderboard', methods=['GET'])
@cross_origin()
def get_leaderboard():
	""" Gets all users from highest wins to lowest.

	Returns:
		list: JSON Success or Error response.
	"""

	def presenter(data):
		""" Formats tuple into list of dicts.

		Args:
			data: List of tuples returned from query.

		Returns:
			list: Array of dict values.
		"""
		for i, (k, v) in enumerate(data):
			yield {
				'user_name': k,
				'wins': int(v)
			}

	# Grab all user name & the count of wins.
	query = db.session.query(
			Account.user_name, func.count(Game.won).label('won')) \
		.filter(Game.won == True) \
		.group_by(Account.user_name) \
		.order_by('won desc') \
		.all()
	return jsonify({'board': list(presenter(query))}), OK_REQUEST
