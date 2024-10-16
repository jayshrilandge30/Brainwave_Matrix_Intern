import sqlite3


def update_product(product_id, new_name, new_quantity, new_price):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Update the name, quantity, and price of the product
    c.execute("UPDATE products SET name = ?, quantity = ?, price = ? WHERE id = ?", (new_name, new_quantity, new_price, product_id))

    conn.commit()
    conn.close()