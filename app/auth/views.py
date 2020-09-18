#!/usr/bin/python3

from flask import render_template, jsonify, request, session, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm, RequestPasswordResetForm, PasswordResetForm
from app import db
from flask_login import login_user, logout_user, login_required, current_user
from ..email import send_mail

@auth.before_app_request
def before_request():
	if current_user.is_authenticated and not current_user.confirmed and request.endpoint[:5] != 'auth.':
		return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
	if current_user.is_anonymous or current_user.confirmed:
		print('unconfirmed')
		return redirect(url_for('index'))
	return render_template('unconfirmed.html')

@auth.route('/confirm')
@login_required
def resend_confirmation():
	token = current_user.generate_confirmation_token()
	send_email('confirm_account', 'Confirm Your Account', current_user, token=token)
	flash('A new confirmation email has been sent to you by email.')
	return redirect(url_for('main.index'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			flash('You have been logged in successfuly')
			return redirect(request.args.get('next') or url_for('index'))
		flash('Invalid email or password')
		return redirect(url_for('auth.login'))
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
		token = user.generate_confirmation_token()
		send_mail(user.email, 'Confirm your account', 'confirm_account', user=user, token=token)
		flash('A confirmation mail has been sent to your mail')
		return redirect(url_for('auth.login'))
	return render_template('register.html', form=form)


@auth.route('/request_password_reset', methods=['GET', 'POST'])
def forgot_password():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RequestPasswordResetForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		token = user.generate_reset_token()
		send_mail(form.email.data, 'Reset your password', 'reset_password', user=user, token=token)
		flash('We have sent an email with details to reset your password')
		return redirect(url_for('auth.login'))
	return render_template('request_password_reset.html', form=form)


@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset(token):
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	form = PasswordResetForm()
	if form.validate_on_submit():
		if User.reset_password(token, form.password.data):
		    db.session.commit()
		    flash('Your password has been updated.')
		    return redirect(url_for('auth.login'))
		else:
		    return redirect(url_for('main.index'))
	return render_template('password_reset.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
	if current_user.confirmed:
		return redirect(url_for('index'))
	if current_user.confirm(token):
		flash('You have confirmed your account successfuly')
	else:
		flash('Your confirmation token os corrupted or has expired')
	return redirect(url_for('index'))


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	flash('You have been logged out successfuly')	
	return redirect(url_for('index'))
