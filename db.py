import sqlite3 

def create_users_table():
    conn = sqlite3.connect('data.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)')
    conn.close()

def add_userdata(username, password):
    conn = sqlite3.connect('data.db')
    conn.execute('INSERT INTO users(username, password) VALUES (?,?)', (username, password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username =? AND password = ?', (username, password))
    data = cursor.fetchone()
    return data
