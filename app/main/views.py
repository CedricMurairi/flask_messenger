from . import main
from flask import render_template, url_for, request, session, jsonify, flash, redirect
from ..models import User, Channel, Connection
from sqlalchemy import or_


@main.route('/', methods=['GET'])
def index():
	if session.get('user'):
		username = session.get('username')
		email = session.get('email')
		user = User.query.filter_by(username=username, email=email).first()
		channel_created = Channel.query.filter_by(channel_creator=user.id).all()
		channel_joined = Channel.query.filter_by(id=user.channel_joined).all()
		connections = Connection.query.filter(or_(Connection.from_id==user.id, Connection.to_id==user.id)).all()

		conversation_user_id = []

		for connection in connections:
			if (connection.from_id == user.id):
				conversation_user.push(connection.to_id)
			if (connection.to_id == user.id):
				conversation_user.push(connection.from_id)

		conversation_user = User.query.filter(User.id.in_(conversation_user_id)).all()

		if channel_created:
			for channel in channel_created:
				print(channel.name, channel.description)
		if channel_joined:
			for channel in channel_joined:
				print(channel.name, channel.description)
		else:
			print('There was nothing in joined channels')
		if user:
			flash('Already logged in')
			return render_template('index.html',conversation_user=conversation_user, channel_joined=channel_joined, channel_created=channel_created, user=user)
	return redirect(url_for('auth.login'))
