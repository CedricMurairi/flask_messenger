#!/usr/bin/python3

from . import db
from datetime import datetime

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(64))
	password = db.Column(db.String(64))
	joined = db.Column(db.DateTime, default=datetime.utcnow)
	is_active = db.Column(db.Boolean, default=False)
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	# db.relationship('Channel', foreign_keys=[Channel.channel_creator], backref='creator', lazy='dynamic')
	channel_joined = db.Column(db.Integer, db.ForeignKey('channels.id'))

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
	from_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
	to_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

class Channel(db.Model):
	__tablename__ = 'channels'
	id = db.Column(db.Integer, primary_key=True)
	channel_creator =  db.Column(db.Integer, db.ForeignKey('users.id'))
	channel_creation = db.Column(db.DateTime, default=datetime.utcnow)
	name = db.Column(db.String(100))
	description = db.Column(db.Text())
	users = db.relationship('User', foreign_keys=[User.channel_joined], backref='channel', lazy='dynamic')