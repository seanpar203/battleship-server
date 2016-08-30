from flask import Blueprint, request

users = Blueprint('users', __name__)


@users.route('/create/', methods=(['POST']))
def create_user():
	return 'Good!'
