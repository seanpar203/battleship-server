import random
from datetime import date

from flask_cors import cross_origin
from flask import Blueprint, jsonify, request
from sqlalchemy import func
from wta_app import db

from wta_app.helpers import add_then_commit, list_of_colors, len_of_colors
from wta_app.models import Host, Time, Account, host_times

times = Blueprint('time', __name__, url_prefix='/api')

OK_REQUEST = 200
BAD_REQUEST = 400


@times.route('/time', methods=(['POST', 'GET']))
@cross_origin()
def create_or_get_time_spent():
	if request.method == 'POST':
		""" POST Request Handler.

		Notes:
			Creates new time spent record for the
			new or existing account.
		"""
		# Get Request Data.
		req = request.json
		host_name = req['host']
		time_spent = req['seconds']
		token = request.headers.get('Authorization')

		# Create new Instances.
		time = Time(time_spent)
		account = Account.get_or_create(token)
		host = Host.get_or_create(host_name)

		# Create Relationships
		account.time_spent.append(time)
		time.host.append(host)

		# Save to DB.
		add_then_commit(account, time, host)
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
		account = Account.get_or_create(token)

		# Define Presenter.
		def results_to_dict(results):
			""" Generates informative dicts from tuples. """
			for i, (key, val) in enumerate(results):
				random_int = random.randrange(len_of_colors)
				yield {
					'label': key,
					'value': int(val),
					'color': list_of_colors[random_int]
				}

		# Get String of Day yyyy-mm-dd
		today = date.isoformat(date.today())

		# Query Instance Time Spent on Web.
		query = db.session.query(
				Host.host_name,
				func.sum(Time.seconds).label('seconds')) \
			.join(host_times, Time) \
			.filter(Time.account_id == account.id) \
			.filter(Time.day == today) \
			.filter(Time.seconds >= 60) \
			.group_by(Host.host_name) \
			.order_by('seconds desc') \
			.all()
		return jsonify({'data': list(results_to_dict(query))})
	else:
		return jsonify({'success': False, 'error': 'no Token'}), BAD_REQUEST
