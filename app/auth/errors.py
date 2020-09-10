from . import auth
from flask import render_template

@auth.app_errorhandler(404)
def handle404(error):
	return render_template('404.html')


@auth.app_errorhandler(500)
def handle500(error):
	return render_template('500.html')


@auth.app_errorhandler(403)
def handle403(error):
	return render_template('403.html')


@auth.app_errorhandler(400)
def handle400(error):
	return render_template('400.html')