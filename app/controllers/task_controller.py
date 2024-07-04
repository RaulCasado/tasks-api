from flask import request, jsonify
from app import db
from app.models.task import Task
from app.models.user import User 

class TaskController:
    @staticmethod
    def get_tasks():
        tasks = Task.query.all()
        task_list = []
        for task in tasks:
            category_names = [category.name for category in task.categories]
            tag_names = [tag.name for tag in task.tags]
            
            task_data = {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'status': task.status,
                'created_at': task.created_at,
                'updated_at': task.updated_at,
                'user_id': task.user_id,
                'username': task.user.username,
                'categories': category_names,
                'tags': tag_names,
            }
            task_list.append(task_data)

        return jsonify(task_list)


    @staticmethod
    def get_task(task_id):
        task = Task.query.get_or_404(task_id)
        category_names = [category.name for category in task.categories]
        tag_names = [tag.name for tag in task.tags]
        
        task_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'created_at': task.created_at,
            'updated_at': task.updated_at,
            'user_id': task.user_id,
            'username': task.user.username,
            'categories': category_names,
            'tags': tag_names,
        }
        
        return jsonify(task_data)


    @staticmethod
    def create_task():
        data = request.get_json()

        user_id = data.get('user_id')

        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            status=data.get('status', 'pending'),
            user_id=user_id
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
