import sqlite3

def get_user_secure(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Correct parameterized query fixing SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()
