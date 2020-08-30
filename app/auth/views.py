#!/usr/bin/python3

from flask import render_template, jsonify, request, session, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from ..models import User
from .forms import InitialForm
from app import db
from sqlalchemy import and_
import json


@auth.app_errorhandler(404)
def handle404(error):
	return render_template('404.html')


@auth.app_errorhandler(500)
def handle500(error):
	return render_template('500.html')


@auth.app_errorhandler(403)
def handle403(error):
	return render_template('403.html')


@auth.app_errorhandler(400)
def handle400(error):
	return render_template('400.html')



@auth.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		print(email, password)
		try:
			user = User.query.filter(and_(User.email==email, User.password==password)).first()
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
		if name and email and password:
			try:
				new_user = User(username=name, email=email, password=password)
				db.session.add(new_user)
			except error:
				flash('An error occured')
				return redirect(url_for('auth.regidter'))
		flash('You cannot register with empty fields')
		return redirect(url_for('auth.register'))
	if session.get('user') is not None:
		return redirect(url_for('index'))
	return render_template('register.html')


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
	if session.get('user') is None:
		flash('Already logged out')
		return redirect(url_for('index'))
	session.pop('user')
	session.pop('username')
	session.pop('email')	
	return redirect(url_for('index'))
