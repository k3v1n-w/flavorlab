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

conn.execute(''' 

INSERT INTO food_item (food_name, description, availability, category, price)  
VALUES ('Garlic Bread', 'Toasted bread with garlic butter', 'Available', 'Starters','3.50'), 
('Tomato Soup','Creamy tomato soup served warm', 'Available', 'Starters','4.00'), 
('Chicken Wings', 'Grilled or crispy chicken wings','Available', 'Starters','5.50'), 
('Mozzarella Sticks','Breaded mozzarella served with dip','Available', 'Starters','4.50'), 
('Bruschetta','Toasted bread with tomato and herbs','Available', 'Starters','4.00'), 
('Nachos','Tortilla chips with cheese and toppings','Available', 'Starters','5.00'), 
('Onion Rings','Crispy battered onion rings','Available','Starters','3.50'), 
('Chicken Strips','Breaded chicken served with dipping sauce','Available', 'Starters','5.50') 

''')
conn.commit()

conn.execute(''' 

CREATE TABLE IF NOT EXISTS order_items ( 
id INTEGER PRIMARY KEY AUTOINCREMENT, 
order_id INTEGER NOT NULL,  
food_item_id INTEGER NOT NULL, 
quantity INTEGER NOT NULL DEFAULT 1, 
FOREIGN KEY (order_id) REFERENCES orders(id), 
FOREIGN KEY (food_item_id) REFERENCES food_item(id) 
)''') 

conn.commit() 

conn.execute(""" 

ALTER TABLE orders RENAME TO orders_old 

""") 

 

# Create new orders table without food_item_id 

conn.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    order_type TEXT NOT NULL CHECK (
        order_type IN ('Delivery', 'Eat In', 'Collection')
    ),
    order_status TEXT NOT NULL DEFAULT 'Pending',
    total_price REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

conn.execute("DROP TABLE IF EXISTS orders_old")
conn.execute("DROP TABLE IF EXISTS menu")

conn.commit()