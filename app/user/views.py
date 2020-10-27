#!/usr/bin/python3

from flask import request, jsonify, render_template ,redirect, url_for, session, flash
from ..models import User, Channel, Connection, MessageUser, MessageChannel, JoinedChannel
from . import user
from .. import db
from .. import socketio
from sqlalchemy import and_, or_, func
from flask_socketio import emit
from flask_login import current_user, login_required
from .forms import CreateChannelForm, SearchUserForm, SearchChannelForm


@user.route("/create-channel", methods=['GET', 'POST'])
@login_required
def create_channel():

	form = CreateChannelForm()
	if form.validate_on_submit():
		channel_name = form.name.data
		channel_description = form.description.data
		channel = Channel(name=channel_name, description=channel_description, channel_creator=current_user.id)
		db.session.add(channel)
		db.session.commit()
		flash('Channel succesfully created')
		return redirect(url_for('user.create_channel'))

	return render_template('create_channel.html', form=form)


@user.route("/join-channel", methods=['GET', 'POST'])
@login_required
def search_channel():
	
	form = SearchChannelForm()
	if form.validate_on_submit():
		channel_name = form.name.data.lower()
		channel_description = form.description.data.lower()
		if channel_name or channel_description:
			channels = Channel.query.filter(or_(func.lower(Channel.name).like("%" +channel_name+ "%"), func.lower(Channel.description).like("%" +channel_description+ "%"))).all()
			if channels:
				return render_template('search_channel.html', form=form, channels=channels)

	return render_template('search_channel.html', form=form)


@user.route("/join-channel/<int:channel_id>", methods=['GET', 'POST'])
@login_required
def join_channel(channel_id):

	joined_channel = JoinedChannel(user_id=current_user.id, channel_id=channel_id)
	db.session.add(joined_channel)
	db.session.commit()
	flash('Successfully joined the channel')
	return redirect(url_for('user.search_channel'))


@user.route("/conversation/users", methods=['GET', 'POST'])
@login_required
def search_user():

	form = SearchUserForm()
	if form.validate_on_submit():
		user_name = form.username.data.lower()
		email = form.email.data.lower()
		
		# return redirect(url_for('user.search_user', username=user_name, email=email))

		# username = request.args.get('username', None)
		# email = request.args.get('email', None)
		if user_name and email:
			users = User.query.filter(or_(func.lower(User.username).like("%" +user_name+ "%"), func.lower(User.email).like("%" +email+ "%"))).all()

			if users:
				return render_template('search_user.html', form=form, users=users)

	return render_template('search_user.html', form=form)


@user.route("/conversation/user/<user_id>", methods=['GET', 'POST'])
@login_required
def join_conversation(user_id):

	connection = Connection(from_id=current_user.id, to_id=user_id)
	db.session.add(connection)
	db.session.commit()
	flash('Successfully connected')
	return redirect(url_for('user.search_user'))


# ===============================================================================
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