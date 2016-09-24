from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from battleship import db

from battleship.helpers import OK_REQUEST, BAD_REQUEST, CREATED, \
	UNAUTHORIZED, \
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


@game.route('/game/<id>', methods=['DELETE'])
@cross_origin()
def delete_game(id):
	""" Delete game.

	Returns:
		dict: JSON Success or Error response.
	"""

	this_game = Game.query.filter_by(id=id).first()
	if this_game is not None:
		Game.query.filter_by(id=id).delete()
		db.session.commit()
		return jsonify({'success': True}), OK_REQUEST
	else:
		return jsonify({'success': False}), BAD_REQUEST


@game.route('/game/<id>/coords', methods=['PUT'])
@cross_origin()
def game_coords(id):
	""" Add user or cpu coordinates to new game.

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


@game.route('/game/<id>/results', methods=['PUT'])
@cross_origin()
def game_results(id):
	""" Update game results.

	Returns:
		dict: JSON Success or Error response.
	"""
	if 'user_name' in request.json:
		# Re-assign request object.
		req = request.get_json()

		# Gather Account & Game related info.
		account = Account.get_or_create(req['user_name'])
		this_game = Game.query.filter_by(id=id).first()

		# Verify request is genuine.
		if this_game.account.id != account.id:
			return jsonify({'success': False}), UNAUTHORIZED
		else:
			# Get or create coordinated for unique game.
			this_game.won = req['won']

			# Save new data.
			add_then_commit(this_game)
			return jsonify({'success': True}), OK_REQUEST
	else:
		return jsonify({'success': False}), BAD_REQUEST
