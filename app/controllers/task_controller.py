from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.task import Task
from app.models.user import User
from app.models.tag import Tag
from app.models.category import Category

class TaskController:
    @staticmethod
    @jwt_required()
    def get_tasks():
        current_user_id = get_jwt_identity()
        tasks = Task.query.filter_by(user_id=current_user_id).all()
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
    @jwt_required()
    def get_task(task_id):
        current_user_id = get_jwt_identity()
        task = Task.query.get_or_404(task_id)
        if task.user_id != current_user_id:
            return jsonify({'error': 'Permission denied'}), 403

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
    @jwt_required()
    def create_task():
        current_user_id = get_jwt_identity()
        data = request.get_json()

        category_ids = data.get('categories', [])
        tag_ids = data.get('tags', [])

        categories = Category.query.filter(Category.id.in_(category_ids)).all()
        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

        if len(categories) != len(category_ids) or len(tags) != len(tag_ids):
            return jsonify({'error': 'Invalid category or tag ID provided'}), 400

        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            status=data.get('status', 'pending'),
            user_id=current_user_id
        )

        new_task.categories.extend(categories)
        new_task.tags.extend(tags)

        db.session.add(new_task)
        db.session.commit()

        return jsonify({'message': 'Task created successfully!'}), 201

    @staticmethod
    @jwt_required()
    def update_task(task_id):
        current_user_id = get_jwt_identity()
        task = Task.query.get_or_404(task_id)
        if task.user_id != current_user_id:
            return jsonify({'error': 'Permission denied'}), 403

        data = request.get_json()
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        db.session.commit()
        return jsonify({'message': 'Task updated successfully!'})

    @staticmethod
    @jwt_required()
    def delete_task(task_id):
        current_user_id = get_jwt_identity()
        task = Task.query.get_or_404(task_id)
        if task.user_id != current_user_id:
            return jsonify({'error': 'Permission denied'}), 403

        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully!'})

    @staticmethod
    @jwt_required()
    def remove_tag_from_task(task_id, tag_id):
        current_user_id = get_jwt_identity()
        task = Task.query.get_or_404(task_id)
        if task.user_id != current_user_id:
            return jsonify({'error': 'Permission denied'}), 403

        tag = Tag.query.get_or_404(tag_id)
        if tag not in task.tags:
            return jsonify({'error': 'Tag is not associated with this task'}), 404

        task.tags.remove(tag)
        db.session.commit()
        
        return jsonify({'message': 'Tag removed from task successfully!'})

    @staticmethod
    @jwt_required()
    def remove_category_from_task(task_id, category_id):
        current_user_id = get_jwt_identity()
        task = Task.query.get_or_404(task_id)
        if task.user_id != current_user_id:
            return jsonify({'error': 'Permission denied'}), 403

        category = Category.query.get_or_404(category_id)
        if category not in task.categories:
            return jsonify({'error': 'Category is not associated with this task'}), 404

        task.categories.remove(category)
        db.session.commit()
        
        return jsonify({'message': 'Category removed from task successfully!'})
