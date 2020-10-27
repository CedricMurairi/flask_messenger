from . import main
from datetime import datetime
from flask import render_template, url_for, request, session, jsonify, flash, redirect
from ..models import User, Channel, Connection
from .. import db
from flask_login import current_user
from sqlalchemy import or_

@main.before_app_request
def ping_user():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.add(current_user)
		db.session.commit()


@main.route('/', methods=['GET'])
def index():
	if current_user.is_anonymous:
		channel_created = None
		channel_joined = None
		connections = None
		conversation_users = None

	if current_user.is_authenticated:
		channel_created = current_user.channels.all()
		channel_joined = current_user.joined_channels.all()
		connections = Connection.query.filter(or_(Connection.from_id==current_user.id, Connection.to_id==current_user.id)).all()

		conversation_user_id = []

		for connection in connections:
			if (connection.from_id == current_user.id):
				conversation_user_id.append(connection.to_id)
			if (connection.to_id == current_user.id):
				conversation_user_id.append(connection.from_id)

		conversation_users = User.query.filter(User.id.in_(conversation_user_id)).all()

	return render_template('index.html',conversation_users=conversation_users, channel_joined=channel_joined, channel_created=channel_created)
