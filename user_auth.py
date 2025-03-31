import sqlite3

# Function to register a user
def register_user(username, password, role="employee"):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()
    conn.close()
    print(f"✅ User '{username}' registered successfully!")

# Function to authenticate a user
def authenticate(username, password):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user
