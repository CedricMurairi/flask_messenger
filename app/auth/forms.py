from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, ValidationError, TextAreaField
from wtforms.validators import InputRequired, EqualTo, Length, Regexp, NumberRange, Email
from email_validator import validate_email

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired()])
	password = PasswordField('Password', validators=[InputRequired()])
	remember_me = BooleanField('Remember me')
	submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
	email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[InputRequired()])
	confirm_password = PasswordField('Confirm password', validators=[InputRequired(), EqualTo('password', 'Passwords must match')])
	submit = SubmitField('Register')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already in use')

class RequestPasswordResetForm(FlaskForm):
	email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
	submit = SubmitField('Request')

	def validate_email(self, field):
		if not User.query.filter_by(email=field.data).first():
			raise ValidationError('Email does not exist in our records')