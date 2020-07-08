#!/usr/bin/python3

from flask import render_template, jsonify, request, session, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from ..models import User
from app import db
import json

@auth.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		print(email, password)
		try:
			user = User.query.filter_by(email=email, password=password).first()
		except Exception as e:
			print(e)
		if user is None:
			flash('Something wrong with you credential')
			return redirect(url_for('.login'))
		session['user'] = True
		session['username'] = user.username
		session['email'] = user.email
		return redirect(url_for('index'))
	if session.get('user') is not None:
		return redirect(url_for('index'))
	return render_template('signin.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		password = request.form.get('password')
		try:
			new_user = User(username=name, email=email, password=password)
			db.session.add(new_user)
		except error:
			flash('An error occured')
			return redirect(url_for('auth.regidter'))
		return redirect(url_for('auth.login'))
	if session.get('user') is not None:
		return redirect(url_for('index'))
	return render_template('register.html')


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
	if session.get('user') is None:
		return jsonify({'logout': True})
	session.pop('user')
	session.pop('username')
	session.pop('email')	
	return redirect(url_for('index'))
