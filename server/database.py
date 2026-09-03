import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

# Create a user table
conn.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    city TEXT,
    phone TEXT,
    role TEXT,
    password TEXT
)''')

# Create a Orders table
conn.execute('''CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    food_item_id INTEGER NOT NULL,
    order_type TEXT NOT NULL CHECK (
        order_type IN ('Delivery', 'Eat In', 'Collection')
    ),
    order_status TEXT NOT NULL DEFAULT 'Pending',
    total_price REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (food_item_id) REFERENCES food(id)
)''')

# Create a Food table
conn.execute('''CREATE TABLE IF NOT EXISTS food_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    food_name TEXT NOT NULL,
    description TEXT NOT NULL,
    availability TEXT NOT NULL
)''')

conn.execute("""
    UPDATE food_item 
    SET price = 6.99 
    WHERE category = 'Dessert'
""")


conn.commit()
 
