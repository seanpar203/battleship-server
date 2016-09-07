from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

from wta_app.helpers import add_then_commit, unique_host_names
from wta_app.models import HostName, TimeSpent, UserToken

times = Blueprint('time', __name__, url_prefix='/api')

OK_REQUEST = 200
BAD_REQUEST = 400


@times.route('/time/', methods=(['POST', 'GET']))
@cross_origin()
def create_or_get_time_spent():

	# POST
	if request.method == 'POST':
		if 'token' in request.json:
			req = request.json

			# Create new Instances.
			time = TimeSpent(req['seconds'])
			user = UserToken.get_or_create(req['token'])
			host = HostName.get_or_create(req['host'])

			# Create Relationships
			user.time_spent.append(time)
			time.host.append(host)

			# Save to DB.
			add_then_commit(user, time, host)
			return jsonify({'success': True}), OK_REQUEST

	# GET
	if request.method == 'GET':
		user = UserToken.query.get(3)
		time = user.time_spent.all()
		hosts = list(set(unique_host_names(time)))
		return jsonify({'list': hosts})
	else:
		return jsonify({'success': False, 'error': 'no Token'}), BAD_REQUEST
