# app/__init__.py
from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app