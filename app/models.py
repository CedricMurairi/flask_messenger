#!/usr/bin/python3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(64))
	password_hash = db.Column(db.String(128))
	joined = db.Column(db.DateTime, default=datetime.utcnow)
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	channels = db.relationship('Channel', backref='creator', lazy='dynamic')
	# direct_messages = db.relationship('MessageUser', backref='users', lazy='dynamic')
	channel_messages = db.relationship('MessageChannel', backref='user', lazy='dynamic')
	# connections = db.relationship('Connection', backref='users', lazy='dynamic')
	joined_channels = db.relationship('JoinedChannel', backref='users', lazy='dynamic')

	@property
	def password(self):
		raise AttributeError('Password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

class MessageUser(db.Model):
	__tablename__ = 'usermessage'
	id = db.Column(db.Integer, primary_key=True)
	to_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	from_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	message = db.Column(db.Text())
	sent = db.Column(db.DateTime, default=datetime.utcnow)
	read = db.Column(db.Boolean, default=False)

class MessageChannel(db.Model):
	__tablename__ = 'channelmessage'
	id = db.Column(db.Integer, primary_key=True)
	to_channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
	from_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	message = db.Column(db.Text())
	sent = db.Column(db.DateTime, default=datetime.utcnow)
	read = db.Column(db.Boolean, default=False)

class Connection(db.Model):
	__tablename__ = 'connections'
	id = db.Column(db.Integer, primary_key=True)
	from_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	to_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class JoinedChannel(db.Model):
	"""docstring for ChannelConnection"""
	__tablename__ = 'joinedchannels'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
		

class Channel(db.Model):
	__tablename__ = 'channels'
	id = db.Column(db.Integer, primary_key=True)
	channel_creator =  db.Column(db.Integer, db.ForeignKey('users.id'))
	channel_creation = db.Column(db.DateTime, default=datetime.utcnow)
	name = db.Column(db.String(100))
	description = db.Column(db.Text())
	messages = db.relationship('MessageChannel', backref='channel', lazy='dynamic')
	users = db.relationship('JoinedChannel', backref='channel', lazy='dynamic')