from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes.task_routes import task_bp
    from .routes.user_routes import user_bp

    app.register_blueprint(task_bp)
    app.register_blueprint(user_bp)

    return app
