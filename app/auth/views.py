#!/usr/bin/python3

from flask import render_template, jsonify, request, g
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from ..models import User
from app import db
import json

@auth.route('/login', methods=['GET', 'POST'])
def login():
	email = request.form.get('email')
	password = request.form.get('password')
	try:
		user = User.query.filter_by(email=email, password=password).first()
	except error:
		print(error)
	if user:
		g.user = user
		return jsonify({'login': True, 'username': user.username, 'email': user.email})
	return jsonify({'login': False})


@auth.route('/register', methods=['GET', 'POST'])
def register():
	name = request.form.get('name')
	email = request.form.get('email')
	password = request.form.get('password')
	try:
		new_user = User(username=name, email=email, password=password)
		db.session.add(new_user)
	except error:
		return jsonify({'registered': False})
	return jsonify({'registered': True})


@auth.route('/logout', methods=['POST'])
def logout():
	if g.user is None:
		return jsonify({'logout': True})
	g.user = None		
	return jsonify({'logout': True})
