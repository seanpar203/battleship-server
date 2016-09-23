from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

from battleship.helpers import BAD_REQUEST, CREATED, UNAUTHORIZED, \
	add_then_commit
from battleship.models import Account, Coords, Game

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
		# Create or get account & create game.
		account = Account.get_or_create(request.json['user_name'])
		new_game = Game()

		# Create relationship & save.
		account.games.append(new_game)
		add_then_commit(account)
		return jsonify({'success': True, 'game_id': new_game.id}), CREATED
	else:
		return jsonify({'success': False}), BAD_REQUEST


@game.route('/game/<id>/coords', methods=['POST'])
@cross_origin()
def game_coords(id):
	""" Add user or cpu positions to new board game.

	Returns:
		dict: JSON Success or Error response.
	"""
	if 'user_name' in request.json:
		# Re-assign request object.
		req = request.json

		# Gather Account & Game related info.
		account = Account.get_or_create(req['user_name'])
		this_game = Game.query.filter_by(id=id).first()

		# Verify request is genuine.
		if this_game.account.id != account.id:
			return jsonify({'success': False}), UNAUTHORIZED
		else:
			# Get or create coordinated for unique game.
			coords = Coords.get_or_create(this_game)
			coords.add_coords(req['player'], req['coords'])

			# Save new data.
			add_then_commit(coords)
			return jsonify({'success': True}), CREATED
	else:
		return jsonify({'success': False}), BAD_REQUEST
