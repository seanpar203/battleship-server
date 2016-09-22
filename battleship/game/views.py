from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

from battleship.helpers import BAD_REQUEST, CREATED, add_then_commit
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
	if 'user_name' in request.json:
		account = Account.get_or_create(request.json['user_name'])
		new_game = Game()
		account.games.append(new_game)
		add_then_commit(account)
		return jsonify({'success': True, 'game_id': new_game.id}), CREATED
	else:
		return jsonify({'success': False}), BAD_REQUEST


@game.route('/game', methods=['GET'])
@cross_origin()
def test_get():
	return jsonify({'success': True}), CREATED
