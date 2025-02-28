import sqlite3

# Connect to the SQLite database
def connect_db():
    return sqlite3.connect('bot_users.db')

# Create the table if it doesn't exist
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            birth_date INTEGER DEFAULT NULL,
            section TEXT DEFAULT NULL,
            region TEXT DEFAULT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert user data into the database
def insert_user():
    # Collecting user data
    print("Enter user details:")
    user_id = input("Enter user ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")

    # Optional fields (can be left blank)
    birth_date = input("Enter birth date (optional, leave blank for NULL): ")
    section = input("Enter section (optional, leave blank for NULL): ")
    region = input("Enter region (optional, leave blank for NULL): ")

    # Convert to correct types
    age = int(age) if age.isdigit() else None
    birth_date = birth_date if birth_date else None
    section = section if section else None
    region = region if region else None

    # Insert data into the database
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (id, name, age, birth_date, section, region)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, name, age, birth_date, section, region))

    conn.commit()
    conn.close()

# Function to query all users in the database
def query_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("\nUsers in the database:")
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    create_table()  # Ensure the table exists
    insert_user()  # Insert user data
    query_users()  # Query and display all users
