from . import main
from datetime import datetime
from flask import render_template, url_for, request, session, jsonify, flash, redirect
from ..models import User, Channel, Connection
from .. import db
from sqlalchemy import or_

@main.before_app_request
def ping_user():
	username = session.get('username')
	email = session.get('email')
	user = User.query.filter_by(username=username, email=email).first()
	if user:
		user.last_seen = datetime.utcnow()
		db.session.add(user)
		db.session.commit()


@main.route('/', methods=['GET'])
def index():
	channel_created = current_user.channels
	channel_joined = current_user.joined_channels
	connections = Connection.query.filter(or_(Connection.from_id==user.id, Connection.to_id==user.id)).all()

	conversation_user_id = []

    for connection in connections:
		if (connection.from_id == user.id):
			conversation_user_id.append(connection.to_id)
		if (connection.to_id == user.id):
			conversation_user_id.append(connection.from_id)

	conversation_users = User.query.filter(User.id.in_(conversation_user_id)).all()

	return render_template('index.html',conversation_users=conversation_users, channel_joined=channel_joined, channel_created=channel_created, user=user)
