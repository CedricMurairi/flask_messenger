#!/usr/bin/python3

from flask import request, jsonify, render_template ,redirect, url_for, session
from ..models import User, Channel, Connection
from . import user
from .. import db


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
		channel_name = request.form.get('search_channel')
		channel = Channel.query.filter_by(name=channel_name).first()

		if(channel):
			print(channel.description)
			return jsonify({'response': True, 'data': {'id': channel.id, 'name': channel.name, 'description': channel.description, 'created': channel.channel_creation, 'creator': channel.channel_creator}})

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
		user = User.query.filter_by(username=username, email=email).first()
		user.joined_channel = channel.id
		db.session.add(user)
		db.session.commit()
		return jsonify({'response': 'Channel joined successfully', 'data': {'name': channel.name, 'description': channel.description, 'created': channel.channel_creation, 'creator': channel.channel_creator}})


@user.route("/conversation/user", methods=['GET', 'POST'])
def search_user():

	if request.method == 'POST':
		search_user_name = request.form.get('search_people')
		user = User.query.filter_by(username=search_user_name).all()

		if(user):
			return jsonify({'response': [{'username': user.username, 'email': user.email, 'joined': user.joined, 'is_active': user.is_active, 'last_seen': user.last_seen} for user in user]})

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


@user.route("/<string:username>/settings", methods=['GET', 'POST'])
def settings(username):

	return '<h2>Hello %s, here is your setting</h2>' %username


@user.route("/<string:username>/profile", methods=['GET', 'POST'])
def profile(username):

	return '<h2>Hello %s, here is your profile</h2>'  %username