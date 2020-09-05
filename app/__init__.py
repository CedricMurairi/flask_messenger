from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config
from flask_socketio import SocketIO

db = SQLAlchemy()
bootstrap = Bootstrap()
socketio = SocketIO()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    socketio.init_app(app)

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