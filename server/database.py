import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")


conn.execute("""
ALTER TABLE orders
ADD table_no INTEGER
""")


conn.commit()



