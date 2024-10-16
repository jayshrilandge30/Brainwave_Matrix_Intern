from tkinter import *
from tkinter import messagebox

from view import view_products

# Function to add a new product to the inventory
def save_product():
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    if name and quantity and price:
        save_product(name, int(quantity), float(price))
        messagebox.showinfo("Success", "Product added to inventory!")
        name_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)
    else:
        messagebox.showwarning("Error", "Please fill in all fields!")

# Function to display all products in the inventory
def display_products():
    products_window = Toplevel(root)
    products_window.title("View Inventory")

    products = view_products()

    for product in products:
        Label(products_window, text=f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}, Price: ${product[3]:.2f}").pack(pady=5)

# Main GUI window
root = Tk()
root.title("Inventory Management System")
root.geometry("400x400")

# Labels and text fields for product name, quantity, and price
Label(root, text="Product Name:", font=("Helvetica", 12)).pack(pady=10)
name_entry = Entry(root, width=40)
name_entry.pack(pady=5)

Label(root, text="Quantity:", font=("Helvetica", 12)).pack(pady=10)
quantity_entry = Entry(root, width=40)
quantity_entry.pack(pady=5)

Label(root, text="Price ($):", font=("Helvetica", 12)).pack(pady=10)
price_entry = Entry(root, width=40)
price_entry.pack(pady=5)

# Buttons to save the product and view all products
Button(root, text="Add Product", command=save_product).pack(pady=10)
Button(root, text="View Inventory", command=display_products).pack(pady=5)

# Run the GUI loop
root.mainloop()