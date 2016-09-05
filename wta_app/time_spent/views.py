from wta_app.models import UserToken, TimeSpent, HostName
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from wta_app import db

times = Blueprint('time', __name__, url_prefix='/api')


@times.route('/time/', methods=(['POST']))
@cross_origin()
def create_time():
	if 'token' in request.json:
		req = request.json
		time = TimeSpent(req['seconds'])
		host = HostName.get_or_create(req['host'])
		user = UserToken.get_or_create(req['token'])
		user.time_spent.append(time)
		time.host.append(host)
		db.session.add(user)
		db.session.add(time)
		db.session.add(host)
		db.session.commit()
		return jsonify({'success': True}), 200
	else:
		return jsonify({'success': False, 'error': 'No Token Value.'}), 400
