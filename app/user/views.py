#!/usr/bin/python3

from flask import request, jsonify, render_template ,redirect, url_for, session

from ..models import User, Channel
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


@user.route("/join-channel", methods=['GET', 'POST'])
def join_channel():

	if request.method == 'POST':
		print('Hey there, here is the post from join-channel route')
		channel_name = request.form.get('search_channel')
		channel = Channel.query.filter_by(name=channel_name).first()

		if(channel):
			print(channel.description)
			return jsonify({'response': 'Channel does exist let\'s check it out'})

		return jsonify({'response': 'No such a channel in our records'})

	return redirect(url_for('index'))


@user.route("/conversation", methods=['GET', 'POST'])
def conversation():

	if request.method == 'POST':
		search_user_name = request.form.get('search_people')
		user = User.query.filter_by(username=search_user_name).all()

		if(user):
			return jsonify({'response': [user.username for user in user]})

		return jsonify({'response': 'No such a user in our records'})

	return redirect(url_for('index'))