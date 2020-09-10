#!/usr/bin/python3

from flask import render_template, jsonify, request, session, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm
from app import db
from flask_login import login_user, logout_user, login_required, current_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and user.verify_password(form.password.data):
			login_user(user)
			flash('You have been logged in successfuly')
			return redirect(request.args.get('next') or url_for('index'))
		flash('Invalid email or password')
		return redirect('auth.login')
		form.email.data = ""
		form.password.data = ""
	return render_template('signin.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data, password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Successfuly registered, you can login')
		redirect(url_for('auth.login'))
	return render_template('register.html', form=form)


@auth.route('/request_password_reset', methods=['GET', 'POST'])
def forgot_password():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RequestPasswordResetForm()
	if form.validate_on_submit():
		# TODO: implement the email sending to let users reset their password
		flash('We have sent an email with the link to reset on your inbox')
		redirect(url_for('auth.forgot_password'))
	return render_template('request_password_reset.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	flash('You have been logged out successfuly')	
	return redirect(url_for('index'))
