import sqlite3


def add_data():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()

    # Insert mock data into Orders table
    orders = [
        ('001', 'Shipped', 'C001'),
        ('002', 'Processing', 'C002'),
        ('003', 'Delivered', 'C003'),
        ('004', 'Cancelled', 'C004'),
        ('005', 'Shipped', 'C005'),
        ('006', 'Processing', 'C006'),
        ('007', 'Delivered', 'C007'),
        ('008', 'Cancelled', 'C008'),
        ('009', 'Shipped', 'C009'),
        ('010', 'Processing', 'C010'),
        ('011', 'Delivered', 'C003'),
        ('012', 'Cancelled', 'C001'),
        ('013', 'Shipped', 'C002'),
        ('014', 'Processing', 'C001'),
        ('015', 'Delivered', 'C001'),
        ('016', 'Cancelled', 'C001')
    ]
    c.executemany('INSERT OR IGNORE INTO Orders VALUES (?, ?, ?)', orders)

    # Insert mock data into Customers table
    customers = [
        ('C001', 'Alice Johnson', 'alice@example.com', '123-456-7890'),
        ('C002', 'Bob Smith', 'bob@example.com', '098-765-4321'),
        ('C003', 'Charlie Brown', 'charlie@example.com', '123-123-1234'),
        ('C004', 'David Williams', 'david@example.com', '456-456-4567'),
        ('C005', 'Eva Davis', 'eva@example.com', '789-789-7890'),
        ('C006', 'Frank Miller', 'frank@example.com', '321-321-4321'),
        ('C007', 'Grace Lee', 'grace@example.com', '654-654-6543'),
        ('C008', 'Hannah Wilson', 'hannah@example.com', '987-987-9876'),
        ('C009', 'Ian Moore', 'ian@example.com', '123-456-1234'),
        ('C010', 'Julia Taylor', 'julia@example.com', '456-789-4567'),
    ]
    c.executemany('INSERT OR IGNORE INTO Customers VALUES (?, ?, ?, ?)', customers)


    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_data()