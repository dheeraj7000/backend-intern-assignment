import sqlite3
from task_model import Task

DATABASE_NAME = 'tasks.db'

def create_tasks_table():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def insert_task(task):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    query = "INSERT INTO tasks (id, title, description, due_date, status) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (task.id, task.title, task.description, task.due_date, task.status))
    connection.commit()
    connection.close()

def get_single_task(task_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    query = "SELECT * FROM tasks WHERE id = ?"
    cursor.execute(query, (task_id,))
    row = cursor.fetchone()
    connection.close()

    if not row:
        return None

    id, title, description, due_date, status = row
    return Task(id, title, description, due_date, status)

def update_single_task(task_id, title, description, due_date, status):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    query = "UPDATE tasks SET title = ?, description = ?, due_date = ?, status = ? WHERE id = ?"
    cursor.execute(query, (title, description, due_date, status, task_id))
    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return False

    connection.close()
    return True

def delete_single_task(task_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    query = "DELETE FROM tasks WHERE id = ?"
    cursor.execute(query, (task_id,))
    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return False

    connection.close()
    return True

def get_task_list(page, per_page):
    offset = (page - 1) * per_page

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    query = "SELECT * FROM tasks LIMIT ? OFFSET ?"
    cursor.execute(query, (per_page, offset))
    rows = cursor.fetchall()
    connection.close()

    return [Task(id, title, description, due_date, status) for id, title, description, due_date, status in rows]
