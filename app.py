from flask import Flask
from task import create_task, get_task, update_task, delete_task, list_tasks
from error_handlers import not_found, bad_request

app = Flask(__name__)

app.register_blueprint(create_task)
app.register_blueprint(get_task)
app.register_blueprint(update_task)
app.register_blueprint(delete_task)
app.register_blueprint(list_tasks)

app.register_error_handler(404, not_found)
app.register_error_handler(400, bad_request)

if __name__ == '__main__':
    from database import create_tasks_table
    create_tasks_table()
    app.run(debug=True)
