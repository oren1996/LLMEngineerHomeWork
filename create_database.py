import sqlite3

def initialize_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()

    # Check if the Orders table already exists
    c.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name='Orders';
    ''')
    orders_table_exists = c.fetchone()

    # Check if the Customers table already exists
    c.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name='Customers';
    ''')
    customers_table_exists = c.fetchone()

    # If the Orders table does not exist, create it
    if not orders_table_exists:
        c.execute('''
            CREATE TABLE IF NOT EXISTS Orders (
                order_id TEXT PRIMARY KEY,
                status TEXT,
                customer_id TEXT
            )
        ''')

    # If the Customers table does not exist, create it
    if not customers_table_exists:
        c.execute('''
            CREATE TABLE IF NOT EXISTS Customers (
                customer_id TEXT PRIMARY KEY,
                name TEXT,
                email TEXT,
                phone TEXT
            )
        ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
