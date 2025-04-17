# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # import models so they’re registered with SQLAlchemy
    from . import models  
    # register our blueprint
    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
