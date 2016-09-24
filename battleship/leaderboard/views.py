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
	query = db.session.query(
			Account.user_name, func.count(Game.won).label('won')) \
		.filter(Game.won == True) \
		.group_by(Account.user_name) \
		.order_by('won desc') \
		.all()
	print(query)
	return jsonify({'success': True, 'leader_board': query}), OK_REQUEST
