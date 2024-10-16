import sqlite3


def view_products():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Select all products from the products table
    c.execute("SELECT * FROM products")
    products = c.fetchall()

    conn.close()
    return products