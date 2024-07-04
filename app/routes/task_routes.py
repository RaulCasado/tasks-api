from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.task_controller import TaskController

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    return TaskController.get_tasks()

@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    return TaskController.get_task(task_id)

@task_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    return TaskController.create_task()

@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    return TaskController.update_task(task_id)

@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    return TaskController.delete_task(task_id)

@task_bp.route('/tasks/<int:task_id>/tags/<int:tag_id>', methods=['DELETE'])
@jwt_required()
def remove_tag_from_task(task_id, tag_id):
    return TaskController.remove_tag_from_task(task_id, tag_id)

@task_bp.route('/tasks/<int:task_id>/categories/<int:category_id>', methods=['DELETE'])
@jwt_required()
def remove_category_from_task(task_id, category_id):
    return TaskController.remove_category_from_task(task_id, category_id)
