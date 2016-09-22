from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

from battleship.helpers import add_then_commit, OK_REQUEST, BAD_REQUEST, CREATED
from battleship.models import Account, Game

# Create new flask blueprint
game = Blueprint('game', __name__)


@game.route('/game', methods=['POST'])
@cross_origin()
def create_game():
	""" Get or Create Account & Create New Game.

	Returns:
		dict: JSON Success or Error response.
	"""
	if 'email' in request.json:
		account = Account.get_or_create(email=request.json['email'])
		new_game = Game()
		account.games.append(new_game)
		add_then_commit(account)
		return jsonify({'success': True, 'game_id': new_game.id}), CREATED
	else:
		return jsonify({'success': False}), BAD_REQUEST
