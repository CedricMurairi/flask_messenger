from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import InputRequired, Email
from email_validator import validate_email
from ..models import Channel

class CreateChannelForm(FlaskForm):
	name = StringField('Channel name', validators=[InputRequired()])
	description = TextAreaField('Channel description', validators=[InputRequired()])
	submit = SubmitField('Create')

	def validate_name(self, field):
		if Channel.query.filter_by(name=field.data).first():
			raise ValidationError('Channel name already in use')


class SearchUserForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired()])
	email = StringField('Email', validators=[Email()])
	submit = SubmitField('Search')


class SearchChannelForm(FlaskForm):
	name = StringField('Channel name', validators=[InputRequired()])
	description = TextAreaField('Channel description')
	submit = SubmitField('Search')