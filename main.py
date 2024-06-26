import sqlite3

def get_user_data(user_id):
    conn = sqlite3.connect('example.db')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = conn.execute(query)
    return result.fetchall()

def execute_code(code):
    eval(code)

execute_code('print(\'hell\')')
get_user_data(232131)