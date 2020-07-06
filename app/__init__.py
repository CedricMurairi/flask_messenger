from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.add_url_rule('/', endpoint='index')
    app.register_blueprint(auth_blueprint)

    @app.route('/hello')
    def hello():
        return '<h2>Hello world. The greatest man on the show</h2>'

    return app