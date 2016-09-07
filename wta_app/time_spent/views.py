from wta_app.models import UserToken, TimeSpent, HostName
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from wta_app.helpers import add_then_commit

times = Blueprint('time', __name__, url_prefix='/api')

OK_REQUEST = 200
BAD_REQUEST = 400


@cross_origin()
@times.route('/time/', methods=(['GET', 'POST']))
def create_or_get_time_spent():
	""" Handle Creating & Getting Time Spent on Web.

	Returns:
		dict: containing successful boolean key.
	"""
	if request.method == 'POST':
		if 'token' in request.json:
			req = request.json

			# Create new Instances.
			time = TimeSpent(req['seconds'])
			host = HostName.get_or_create(req['host'])
			user = UserToken.get_or_create(req['token'])

			# Create Relationships
			user.time_spent.append(time)
			time.host.append(host)

			# Save to DB.
			add_then_commit(user, time, host)
		return jsonify({'success': True}), OK_REQUEST
	else:
		return jsonify({'success': False, 'error': 'no Token'}), BAD_REQUEST
