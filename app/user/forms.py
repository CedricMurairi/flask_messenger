from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, ValidationError, TextAreaField
from wtforms.validators import InputRequired, EqualTo, Length, Regexp, NumberRange, Email
from email_validator import validate_email
from ..models import User

class CreateChannelForm(FlaskForm):
	name = StringField('Channel name', validators=[InputRequired()])
	description = TextAreaField('Channel description', validators=[InputRequired()])
	submit = SubmitField('Create')

	def validate_name(self):
		if Channel.query.filter_by(name=name).first():
			aise ValidationError('Channel name already in use')


class SearchUserForm(FlaskForm):
	username = StringField('Username')
	email = StringField('Email')
	submit = SubmitField('Search')


class SearchChannelForm(FlaskForm):
	name = StringField('Channel name', validators=[InputRequired()])
	description = TextAreaField('Channel description', validators=[InputRequired()])
	submit = SubmitField('Search')