#!/usr/bin/python3

from flask import request, jsonify, render_template ,redirect, url_for, session

from ..models import User, Channel
from . import user
from .. import db


@user.route("/create-channel", methods=['GET', 'POST'])
def create_channel():
	if request.method == 'POST':
		channel_name = request.form.get('channel_name')
		channel_description = request.form.get('channel_description')
		username = session.get('username')
		email = session.get('email')
		channel_creator = User.query.filter_by(username=username, email=email).first()
		if(channel_creator):
			new_channel = Channel(name=channel_name, description=channel_description, channel_creator=channel_creator.id)
			db.session.add(new_channel)
			db.session.commit()
		return jsonify({'response': 'Post content recieved'})
	return redirect(url_for('index'))


@user.route("/join-channel", methods=['GET', 'POST'])
def join_channel():
	if request.method == 'POST':
		channel_name = request.form.get('search_channel')
		channels = Channel.query,filter_by(name=channel_name).all()
		if(channels):
			for channel in channels:
				print(channel.description)
		return jsonify({'response': 'Post content recieved'})
	return redirect(url_for('index'))


@user.route("/conversation", methods=['GET', 'POST'])
def conversation():
	if request.method == 'POST':
		return jsonify({'response': 'Post content recieved'})
	return redirect(url_for('index'))