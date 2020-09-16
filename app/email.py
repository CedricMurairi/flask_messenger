from flask_mail import Mail, Message
from . import mail
from flask import render_template, current_app
from threading import Thread
import os
import smtplib


# def send_async_mail(msg):
# 	with app.app_context():
# 		mail.send(msg)


def send_mail(to, subject, template, **kwargs):
	msg = Message('[Flask Messenger]' + subject, sender='Cedric Murairi <murairicedric@gmail.com>', recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	# thr = Thread(target=send_async_mail, args=[msg])
	# thr.start()

	mail.send(msg)

	# return thr
