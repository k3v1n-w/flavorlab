import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

# Create a user table
conn.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    city TEXT,
    phone TEXT
)''')

# Create a orders table
conn.execute('''CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    status TEXT NOT NULL,
    total TEXT,
    created TEXT
)''')

 