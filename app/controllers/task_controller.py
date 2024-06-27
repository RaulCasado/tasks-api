from flask import request, jsonify
from app import db
from app.models.task import Task

class TaskController:
    @staticmethod
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'created_at': task.created_at,
            'updated_at': task.updated_at
        } for task in tasks])

    @staticmethod
    def get_task(task_id):
        task = Task.query.get_or_404(task_id)
        return jsonify({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'created_at': task.created_at,
            'updated_at': task.updated_at
        })

    @staticmethod
    def create_task():
        data = request.get_json()
        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            status=data.get('status', 'pending')
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully!'}), 201

    @staticmethod
    def update_task(task_id):
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        db.session.commit()
        return jsonify({'message': 'Task updated successfully!'})

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully!'})
