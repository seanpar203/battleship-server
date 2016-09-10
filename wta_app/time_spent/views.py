from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from wta_app import db

from sqlalchemy import func

from wta_app.helpers import add_then_commit, results_to_dict
from wta_app.models import HostName, TimeSpent, UserToken, host_times

times = Blueprint('time', __name__, url_prefix='/api')

OK_REQUEST = 200
BAD_REQUEST = 400


@times.route('/time/', methods=(['POST', 'GET']))
@cross_origin()
def create_or_get_time_spent():
	if request.method == 'POST':
		""" POST Request Handler.

		Notes:
			Creates new time spent record for the
			new or existing user.
		"""
		# Get Request Data.
		req = request.json
		host_name = req['host']
		time_spent = req['seconds']
		token = request.headers.get('Authorization')

		# Create new Instances.
		time = TimeSpent(time_spent)
		user = UserToken.get_or_create(token)
		host = HostName.get_or_create(host_name)

		# Create Relationships
		user.time_spent.append(time)
		time.host.append(host)

		# Save to DB.
		add_then_commit(user, time, host)
		return jsonify({'success': True}), OK_REQUEST

	# GET
	if request.method == 'GET':
		""" GET Request Handler.

		Notes:
			Grabs all host name records and the time spent,
			associated with them within the current day.
		"""
		# Get Request Data.
		token = request.headers.get('Authorization')

		# Grab Instance.
		user = UserToken.get_or_create(token)

		# Query Instance Time Spent on Web.
		query = db.session.query(
				HostName.host_name.label('host_name'),
				func.sum(TimeSpent.seconds).label('elapsed_time')) \
			.join(host_times, TimeSpent) \
			.filter(TimeSpent.user_id == user.id) \
			.group_by(HostName.host_name) \
			.all()
		return jsonify({'data': list(results_to_dict(query))})
	else:
		return jsonify({'success': False, 'error': 'no Token'}), BAD_REQUEST
