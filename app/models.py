#!/usr/bin/python3

from . import db
from datetime import datetime

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(64))
	password = db.Column(db.String(64))
	joined = db.Column(db.DateTime)
	own_channel = db.Column(db.Integer, db.ForeignKey('channels.id'))


class Channel(db.Model):
	__tablename__ = 'channels'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	description = db.Column(db.Text())
	users = db.relationship('User', backref='Channel', lazy='dynamic')