from . import main
from flask import render_template, url_for, request, session, jsonify, flash, redirect
from ..models import User


@main.route('/', methods=['GET','POST'])
def index():
	if session.get('user'):
		username = session.get('username')
		email = session.get('email')
		user = User.query.filter_by(username=username, email=email).first()
		if user:
			flash('Already logged in')
			return render_template('index.html', username=user.username, email=user.email)
	return redirect(url_for('auth.login'))
