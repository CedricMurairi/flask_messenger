import os
from app import create_app, db
from app.models import User, MessageUser
from flask_script import Manager, Shell
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

# login_manager = LoginManager(app)

# login_manager.session_protection = 'strong'
# login_manager.loginview = 'index'

# @login_manager.user_loader
# def load_user(user_id):
# 	return User.query.get(int(user_id))

@manager.command
def create_table():
	"""Create tables"""
	db.create_all()
	print('Tables created')

@manager.command
def test():
	"""Run the unit tests."""
	import unittest
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

def make_shell_context():
    return dict(app=app, db=db, user=User)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    with app.app_context():
        manager.run()
