from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Route to display the form
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user-form')
def user_form():
    return render_template('user-form.html')

@app.route('/order')
def order_form():
    return render_template('order.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')



# Route to handle form submission (POST)
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        phone = request.form['phone']

        try:
            # Connect to database
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Insert data into table
            cursor.execute('''INSERT INTO users (name, email, city, phone) 
                            VALUES (?, ?, ?, ?)''', 
                          (name, email, city, phone))

            conn.commit()
            conn.close()

            return redirect(url_for('success'))
        except Exception as e:
            return f"Error: {e}"

# Route to display success message
@app.route('/success')
def success():
    return render_template('success.html')

# Route to view all submitted data
@app.route('/users')
def users():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users_data = cursor.fetchall()
        conn.close()
        return render_template('users.html', users=users_data)
    except Exception as e:
        return f"Error: {e}"

# Route to view all submitted data
@app.route('/orders')
def orders():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders')
        orders_data = cursor.fetchall()
        conn.close()
        return render_template('orders.html', orders=orders_data)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)

# Route to handle form submission (POST)
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        phone = request.form['phone']

        try:
            # Connect to database
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Insert data into table
            cursor.execute('''INSERT INTO users (name, email, city, phone) 
                            VALUES (?, ?, ?, ?)''', 
                          (name, email, city, phone))

            conn.commit()
            conn.close()

            return redirect(url_for('success'))
        except Exception as e:
            return f"Error: {e}"

# Route to handle form submission (POST)
@app.route('/submit-orders', methods=['POST'])
def submit_orders():
    if request.method == 'POST':
        # Get form data
        order_type = request.form['order_type']
        created = request.form['created']
        #total_price = request.form['']
        
        try:
            # Connect to database
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Insert data into table
            cursor.execute('''INSERT INTO users (order_type, created) 
                            VALUES (?, ?, ?, ?)''', 
                          (order_type, created))

            conn.commit()
            conn.close()

            return redirect(url_for('success'))
        except Exception as e:
            return f"Error: {e}"
