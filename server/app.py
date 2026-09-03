from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('restaurant.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user-form')
def user_form():
    return render_template('user-form.html')


#@app.route('/menu')
#def menu():
#   return render_template('menu.html')

@app.route('/about-us')
def aboutUs():
    return render_template('about-us.html')

@app.route('/order')
def order():
    return render_template('order.html')

'''
@app.route("/order-test", methods=["GET", "POST"])
def order():

    conn = get_db_connection()

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
    food_items = conn.execute(
        "SELECT * FROM food_item WHERE availability = 'Available'"
    ).fetchall()

    conn.close()

    return render_template("order.html", food_items=food_items)
    '''
 

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

# Route to view all submitted data
@app.route('/menu')
def menu():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM food_item WHERE category = "Main Meal"')
        food_mainMeal = cursor.fetchall()
        cursor.execute('SELECT * FROM food_item WHERE category = "Drinks"')
        food_Drinks = cursor.fetchall()
        cursor.execute('SELECT * FROM food_item WHERE category = "Dessert"')
        food_Desserts = cursor.fetchall()
        conn.close()
        return render_template('menu.html', foodMain=food_mainMeal, foodDrinks=food_Drinks, foodDesserts=food_Desserts)
    except Exception as e:
        return f"Error: {e}"
'''
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
'''




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

if __name__ == '__main__':
    app.run(debug=True)
