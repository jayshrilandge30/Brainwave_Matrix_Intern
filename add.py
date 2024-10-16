import sqlite3


def add_product(name, quantity, price):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Insert the new product into the products table
    c.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))

    conn.commit()
    conn.close()