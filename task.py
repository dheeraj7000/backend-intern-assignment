from flask import Blueprint, jsonify, request, abort
import uuid
from database import insert_task, get_single_task, update_single_task, delete_single_task, get_task_list
from task_model import Task

create_task = Blueprint('create_task', __name__)
get_task = Blueprint('get_task', __name__)
update_task = Blueprint('update_task', __name__)
delete_task = Blueprint('delete_task', __name__)
list_tasks = Blueprint('list_tasks', __name__)


@create_task.route('/tasks', methods=['POST'])
def create_task_route():
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data or 'due_date' not in data:
        abort(400, "Invalid data. Title, description, and due_date are required.")

    id = str(uuid.uuid4())
    title = data['title']
    description = data['description']
    due_date = data['due_date']
    status = data.get('status', 'Incomplete')

    task = Task(id, title, description, due_date, status)
    insert_task(task)

    return jsonify({"message": "Task created successfully.", "task_id": task.id}), 201


@get_task.route('/tasks/<string:task_id>', methods=['GET'])
def get_task_route(task_id):
    task = get_single_task(task_id)
    if not task:
        abort(404, "Task not found.")

    return jsonify(task.__dict__)


@update_task.route('/tasks/<string:task_id>', methods=['PUT'])
def update_task_route(task_id):
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data or 'due_date' not in data:
        abort(400, "Invalid data. Title, description, and due_date are required.")

    success = update_single_task(task_id, data['title'], data['description'], data['due_date'], data.get('status', 'Incomplete'))
    if not success:
        abort(404, "Task not found.")

    return jsonify({"message": "Task updated successfully."})


@delete_task.route('/tasks/<string:task_id>', methods=['DELETE'])
def delete_task_route(task_id):
    success = delete_single_task(task_id)
    if not success:
        abort(404, "Task not found.")

    return jsonify({"message": "Task deleted successfully."})


@list_tasks.route('/tasks', methods=['GET'])
def list_tasks_route():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    tasks = get_task_list(page, per_page)

    return jsonify([task.__dict__ for task in tasks])
