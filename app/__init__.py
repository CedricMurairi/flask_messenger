from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config
from flask_socketio import SocketIO
from flask_mail import Mail
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
socketio = SocketIO()
moment = Moment()
mail = Mail()
login_manager = LoginManager()

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__, static_folder="statics")
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    socketio.init_app(app)
    moment.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .user import user as user_blueprint

    app.register_blueprint(main_blueprint)
    app.add_url_rule('/', endpoint='index')
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)

    @app.route('/hello')
    def hello():
        return '<h2>Hello world. The greatest man on the show</h2>'

    return app