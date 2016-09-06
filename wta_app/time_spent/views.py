from wta_app.models import UserToken, TimeSpent, HostName
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from wta_app import db

BAD_REQUEST = 400
OK_REQUEST = 200

times = Blueprint('time', __name__, url_prefix='/api')


@times.route('/time/', methods=(['GET', 'POST']))
@cross_origin()
def create_time():
	# if request.module == 'GET':
	# 	if 'token' in request.json:
	# 		req = request.json
	# 		user = UserToken.get_or_create(req['token'])
	# 	else:
	# 		return jsonify({'success': False}), BAD_REQUEST
	if request.method == 'POST':
		if 'token' in request.json:
			req = request.json
			user = UserToken.get_or_create(req['token'])

			time = TimeSpent(req['seconds'])
			host = HostName.get_or_create(req['host'])
			user.time_spent.append(time)
			time.host.append(host)
			db.session.add(user)
			db.session.add(time)
			db.session.add(host)
			db.session.commit()
			return jsonify({'success': True}), OK_REQUEST
		else:
			return jsonify({'success': False, 'error':   'No Token Value.'}), BAD_REQUEST
