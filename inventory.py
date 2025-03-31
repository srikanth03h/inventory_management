import sqlite3

# Function to add a new product
def add_product(name, quantity, price):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    conn.close()
    print(f"✅ Product '{name}' added successfully!")

# Function to view all products
def view_products():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

# Function to update stock
def update_stock(product_id, new_quantity):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()
    conn.close()
    print(f"✅ Product ID {product_id} stock updated to {new_quantity}")

# Function to delete a product
def delete_product(product_id):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    print(f"❌ Product ID {product_id} deleted.")
