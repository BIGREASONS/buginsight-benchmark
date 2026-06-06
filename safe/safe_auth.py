import sqlite3
import hashlib
import os

def authenticate_user(username, password):
    # Uses strong crypto and parameterized queries
    salt = os.urandom(32)
    hashed_pw = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, hashed_pw))
    return cursor.fetchone()
