from wta_app.models import UserToken
from flask import Blueprint, request, jsonify
from wta_app import db

users = Blueprint('users', __name__, url_prefix='/user')


@users.route('/create/', methods=(['POST']))
def create_user():
	if 'token' in request.json:
		token = request.json['token']
		return jsonify({'success': True})
	else:
		return jsonify({'success': False})
