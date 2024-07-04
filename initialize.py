from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

hostname = os.getenv("HOSTNAME")
database = os.getenv("DATABASE")
port = os.getenv("PORT")
username = os.getenv("DB_USERNAME")
password = os.getenv("PASSWORD")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Enum('pending', 'in_progress', 'completed'), default='pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

class TaskCategory(db.Model):
    task_id = db.Column(db.Integer, db.ForeignKey('task.id', ondelete='CASCADE'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete='CASCADE'), primary_key=True)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

class TaskTag(db.Model):
    task_id = db.Column(db.Integer, db.ForeignKey('task.id', ondelete='CASCADE'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id', ondelete='CASCADE'), primary_key=True)

@app.route('/initialize')
def initialize():
    with app.app_context():
        db.create_all()

        # Add categories
        categories = ['Trabajo', 'Personal', 'Estudios', 'Salud', 'Proyectos', 'Finanzas', 'Compras', 'Viajes']
        for name in categories:
            category = Category(name=name)
            db.session.add(category)

        # Add tags
        tags = ['Urgente', 'Importante', 'Baja Prioridad', 'Largo Plazo', 'Corto Plazo']
        for name in tags:
            tag = Tag(name=name)
            db.session.add(tag)

        db.session.commit()

    return "Database initialized with categories and tags."

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
