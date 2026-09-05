from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user-form')
def user_form():
    return render_template('user-form.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/order-success')
def order_success():
    return render_template('order-success.html')

# Route to handle making an order (GET and POST)
@app.route("/order", methods=["GET", "POST"])
def order():

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    if request.method == "POST":

        # Get selected food item IDs
        selected_items = request.form.getlist("food_items")

        # Get order type
        order_type = request.form.get("order_type")

        # Example user ID
        # Later you can get this from the logged-in user
        user_id = 1

        # Make sure food was selected
        if not selected_items:
            conn.close()
            return "Please select at least one food item."

        total_price = 0

        # Create the order first
        cursor = conn.execute("""
            INSERT INTO orders
            (user_id, order_type, order_status, total_price)
            VALUES (?, ?, ?, ?)
        """, (user_id, order_type, "Pending", total_price))

        # Get the ID of the newly created order
        order_id = cursor.lastrowid

        # Add each selected food item
        for food_item_id in selected_items:

            conn.execute("""
                INSERT INTO order_items
                (order_id, food_item_id, quantity)
                VALUES (?, ?, ?)
            """, (order_id, food_item_id, 1))

        conn.commit()
        conn.close()

        return redirect(url_for("order_success"))

    # GET request - get food items
    starter_items = conn.execute(
        "SELECT * FROM food_item WHERE availability = 'Available' AND category = 'Starters' "
    ).fetchall()

    main_items = conn.execute(
        "SELECT * FROM food_item WHERE availability = 'Available' AND category = 'Main Meal'"
    ).fetchall()

    side_items = conn.execute(
        "SELECT * FROM food_item WHERE availability = 'Available' AND category = 'Sides'"
    ).fetchall()

    dessert_items = conn.execute(
        "SELECT * FROM food_item WHERE availability = 'Available' AND category = 'Dessert'"
    ).fetchall()

    conn.close()

    return render_template("order.html", starters=starter_items, mains=main_items, sides=side_items , desserts=dessert_items)


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

# Route to handle form submission (POST)
@app.route('/submit-orders', methods=['POST'])
def submit_orders():
    if request.method == 'POST':
        # Get form data
        order_type = request.form['order_type']
        #total_price = request.form['']

        try:
            # Connect to database
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Insert data into table
            cursor.execute('''INSERT INTO orders (order_type, created) 
                            VALUES (?, ?, ?, ?)''', 
                          (order_type, created))

            conn.commit()
            conn.close()

            return redirect(url_for('success'))
        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
 