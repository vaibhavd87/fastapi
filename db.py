import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()

# Create table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')

# Add a new user
def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username, password) VALUES (?,?)', (username, password))
    conn.commit()

# Login function
def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data

# Check if user exists
def check_user(username):
    c.execute('SELECT * FROM userstable WHERE username =?', (username,))
    data = c.fetchall()
    return data
