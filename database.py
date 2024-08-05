import sqlite3

def create_connection():
    conn = sqlite3.connect('tasks.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        is_completed INTEGER NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

def add_task(title, description):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(id, title, description, is_completed):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET title = ?, description = ?, is_completed = ? WHERE id = ?', (title, description, is_completed, id))
    conn.commit()
    conn.close()

def delete_task(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
