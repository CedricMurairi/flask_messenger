#!/usr/bin/python3

from flask import request, jsonify, render_template

from . import user


@user.route("/create-channel", methods=['GET', 'POST'])
def create_channel():
	if request.method == 'POST':
		return jsonify({'response': 'Post content recieved'})
	return render_template('create_channel.html', username='cedric murairi')


@user.route("/join-channel", methods=['GET', 'POST'])
def join_channel():
	if request.method == 'POST':
		return jsonify({'response': 'Post content recieved'})
	return render_template('join_channel.html', username='cedric murairi')


@user.route("/conversation", methods=['GET', 'POST'])
def conversation():
	if request.method == 'POST':
		return jsonify({'response': 'Post content recieved'})
	return render_template('conversation.html', username='cedric murairi')