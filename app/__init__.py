import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'default_secret_key')
    
    jwt = JWTManager(app)

    db.init_app(app)

    from .routes.task_routes import task_bp
    from .routes.user_routes import user_bp

    app.register_blueprint(task_bp)
    app.register_blueprint(user_bp)

    return app
