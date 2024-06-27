from app import db
from .task_category import task_category
from .task_tag import task_tag
from .category import Category
from .tag import Tag

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Enum('pending', 'in_progress', 'completed'), default='pending')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    categories = db.relationship('Category', secondary=task_category, backref=db.backref('tasks', lazy='dynamic'))
    tags = db.relationship('Tag', secondary=task_tag, backref=db.backref('tasks', lazy='dynamic'))
