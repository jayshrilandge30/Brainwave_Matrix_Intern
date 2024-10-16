def delete_product(product_id):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Delete the product from the products table
    c.execute("DELETE FROM products WHERE id = ?", (product_id,))

    conn.commit()
    conn.close()