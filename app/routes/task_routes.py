from flask import Blueprint
from app.controllers.task_controller import TaskController

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return TaskController.get_tasks()

@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return TaskController.get_task(task_id)

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    return TaskController.create_task()

@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    return TaskController.update_task(task_id)

@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return TaskController.delete_task(task_id)
