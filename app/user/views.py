#!/usr/bin/python3

from flask import request, jsonify, render_template ,redirect, url_for, session
from ..models import User, Channel, Connection, MessageUser, MessageChannel
from . import user
from .. import db
from sqlalchemy import and_, or_, func


@user.route("/create-channel", methods=['GET', 'POST'])
def create_channel():

	if request.method == 'POST':
		print('Hey there, here is the post from create-channel route')
		channel_name = request.form.get('channel_name')
		channel_description = request.form.get('channel_description')
		username = session.get('username')
		email = session.get('email')
		channel_creator = User.query.filter_by(username=username, email=email).first()

		if(channel_creator):
			check_channel = Channel.query.filter_by(name=channel_name).first()

			if(check_channel):
				return jsonify({'response': 'Channel already in our records'})

			new_channel = Channel(name=channel_name, description=channel_description, channel_creator=channel_creator.id)
			db.session.add(new_channel)
			db.session.commit()
			return jsonify({'response': 'Channel created successfully'})

	return redirect(url_for('index'))


@user.route("/join-channel/channels", methods=['GET', 'POST'])
def search_channel():
	if request.method == 'POST':
		print('Hey there, here is the post from join-channel route')
		channel_name = request.form.get('search_channel').lower()
		channels = Channel.query.filter(func.lower(Channel.name).like('%' +channel_name+ '%')).all()

		if(channels):
			return jsonify({'response': [{'id': channel.id, 'name': channel.name, 'description': channel.description, 'created': channel.channel_creation, 'creator': channel.channel_creator} for channel in channels]})

		return jsonify({'response': 'No such a channel in our records'})

	return redirect(url_for('index'))


@user.route("/join-channel/channels/join", methods=['POST'])
def join_channel():
	print('Hey there, here is the post from join-channel route')
	channel_id = request.form.get('channel_id')
	channel = Channel.query.filter_by(id=channel_id).first()

	if(channel):
		username = session.get('username')
		email = session.get('email')
		user = User.query.filter(and_(User.username==username, User.email==email)).first()
		print(user.username, user.email)
		user.channel_joined = channel.id
		db.session.add(user)
		db.session.commit()
		return jsonify({'response': 'Channel joined successfully', 'data': {'name': channel.name, 'description': channel.description, 'created': channel.channel_creation, 'creator': channel.channel_creator}})


@user.route("/conversation/user", methods=['GET', 'POST'])
def search_user():

	if request.method == 'POST':
		user_name = session.get('username')
		user_email = session.get('email')
		search_user_name = request.form.get('search_people').lower()
		user = User.query.filter(and_(func.lower(User.username).like("%" +search_user_name+ "%"), User.username != user_name, User.email != user_email)).all()

		if(user):
			return jsonify({'response': [{'id': user.id, 'username': user.username, 'email': user.email, 'joined': user.joined, 'is_active': user.is_active, 'last_seen': user.last_seen} for user in user]})

		return jsonify({'response': 'No such a user in our records'})

	return redirect(url_for('index'))


@user.route("/conversation/user/join", methods=['POST'])
def join_conversation():

	user_connection = request.form.get('user_id')
	if(user_connection):
		username = session.get('username')
		email = session.get('email')
		user = User.query.filter_by(username=username, email=email).first()
		connection = Connection(from_id=user.id, to_id=user_connection)
		db.session.add(connection)
		db.session.commit()

		return jsonify({'response': 'Connection created successfully'})


@user.route('/fetch/direct/messages', methods=['GET', 'POST'])
def fetch_direct_message():

	 if request.method == 'POST':
	 	connection_id = request.form.get('connection_id')
	 	current_user_id = request.form.get('current_user_id')
	 	messages = MessageUser.query.filter(and_(or_(MessageUser.from_id==connection_id, MessageUser.to_id==connection_id), or_(MessageUser.from_id==current_user_id, MessageUser.to_id==current_user_id))).all()

	 	if messages:
	 		for message_item in messages:
	 			print(message_item.id, message_item.message)

	 		return {'backup': {'connection_user': connection_id, 'current_user': current_user_id}, 'response': [{'connection_user': connection_id, 'current_user': current_user_id, 'from_id': message.from_id, 'to_id': message.to_id, 'from_user': User.query.filter_by(id=message.from_id).first().username, 'to_user': User.query.filter_by(id=message.to_id).first().username, 'body': message.message, 'sent': message.sent} for message in messages]}

	 	return {'backup': {'connection_user': connection_id, 'current_user': current_user_id}, 'response': 'There are no message thread for current user'}

	 return redirect(url_for('index'))

@user.route('/fetch/channel/messages', methods=['GET', 'POST'])
def fetch_channel_message():

	 if request.method == 'POST':
	 	channel_id = request.form.get('channel_id')
	 	messages = MessageChannel.query.filter_by(to_channel_id=channel_id).all()
	 	username = session.get('username')
	 	email = session.get('email')
	 	current_user = User.query.filter(and_(User.username==username, User.email==email)).first()

	 	if messages:
		 	for message in messages:
		 		print(message.from_id, message.message)
	 		return {'backup': {'channel_id': message.to_channel_id, 'current_user': current_user.id}, 'response': [{'channel_id': message.to_channel_id, 'channel_name': Channel.query.filter_by(id=message.to_channel_id).first().name , 'current_user': current_user.id, 'from_id': message.from_id, 'from_user': User.query.filter_by(id=message.from_id).first().username, 'body': message.message, 'sent': message.sent} for message in messages]}
	 	print('The channel id is:', channel_id)
	 	return {'backup': {'channel_id': channel_id, 'current_user': current_user.id}, 'response': 'The server got your response for channel messages'}

	 return redirect(url_for('index'))


@user.route('/send/message', methods=['POST'])
def send_message():
	message_type = request.form.get('message_type')
	if message_type == "direct":
		from_id = request.form.get('from_user_id')
		to_id = request.form.get('to_user_id')
		message = request.form.get('message')
		new_message = MessageUser(from_id=from_id, to_id=to_id, message=message)
		db.session.add(new_message)
		db.session.commit()

		message_saved = MessageUser.query.filter(and_(MessageUser.from_id==from_id, MessageUser.to_id==to_id, MessageUser.message==message)).first()
		time = message_saved.sent
		sender = User.query.filter_by(id=from_id).first().username
		print(message, message_saved.message)

		return {'response': {'from_user': sender, 'message': message, 'sent': time}}

	if message_type == "channel":
		from_id = request.form.get('from_user_id')
		to_channel_id = request.form.get('to_channe_id')
		message = request.form.get('message')
		new_message = MessageChannel(from_id=from_id, to_channel_id=to_channel_id, message=message)
		db.session.add(new_message)
		db.session.commit()

		message_saved = MessageChannel.query.filter(and_(MessageChannel.from_id==from_id, MessageChannel.to_channel_id==to_channel_id, MessageChannel.message==message)).first()
		time = message_saved.sent
		sender = User.query.filter_by(id=from_id).first().username
		print(message, message_saved.message)

		return {'response': {'from_user': sender, 'message': message, 'sent': time}}


@user.route("/<string:username>/settings", methods=['GET', 'POST'])
def settings(username):

	return render_template('under_dev.html', username=username)


@user.route("/<string:username>/profile", methods=['GET', 'POST'])
def profile(username):

	return render_template('under_dev.html', username=username)