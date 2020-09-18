#!/usr/bin/python3
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from flask import current_app
from . import db
from datetime import datetime
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(64))
	password_hash = db.Column(db.String(128))
	joined = db.Column(db.DateTime, default=datetime.utcnow)
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	confirmed = db.Column(db.Boolean, default=False)
	channels = db.relationship('Channel', backref='creator', lazy='dynamic')
	# direct_sent_messages = db.relationship('MessageUser', foreign_keys=[MessageUser.from_id], backref=db.backref('sender', lazy='joined'), lazy='dynamic', cascade='all, delete-orphan')
	# direct_received_messages = db.relationship('MessageUser', foreign_keys=[MessageUser.to_id], backref=db.backref('receiver', lazy='joined'), lazy='dynamic', cascade='all, delete-orphan')
	channel_messages = db.relationship('MessageChannel', backref='user', lazy='dynamic')
	# connections = db.relationship('Connection', foreign_keys=['Connection.from_id'], backref=db.backref('connector', lazy='joined'), lazy='dynamic', cascade='all, delete-orphan')
	# connected = db.relationship('Connection', foreign_keys=['Connection.to_id'], backref=db.backref('connections', lazy='joined'), lazy='dynamic', cascade='all, delete-orphan')
	joined_channels = db.relationship('JoinedChannel', backref='users', lazy='dynamic')

	@property
	def password(self):
		raise AttributeError('Password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def generate_confirmation_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
		return s.dumps({'confirm': self.id})

	def generate_reset_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
		return s.dumps({'reset': self.id})

	@staticmethod
	def reset_password(token, new_password):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
			print(data)
		except:
			return False
		user = User.query.get(data.get('reset'))
		if user is None:
			return False
		user.password = new_password
		db.session.add(user)
		return True

	def confirm(self, token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except:
			return False

		if data.get('confirm') != self.id:
			return False

		self.confirmed = True
		db.session.add(self)
		db.session.commit()
		return True


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