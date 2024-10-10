import customtkinter as ctk
from PIL import Image, ImageTk

# Create the main window
root = ctk.CTk()
root.title("E-Shop Interface")
root.geometry("800x600")

# Sample product data with image paths
products = {
    "Product 1": {"price": 10.99, "image": "D:\Python\School\class12final\Screenshot 2023-05-17 184015.png"},
    "Product 2": {"price": 15.49, "image": "D:\Python\School\class12final\Screenshot 2023-05-17 184015.png"},
    "Product 3": {"price": 7.99, "image": "D:\Python\School\class12final\Screenshot 2023-05-17 184015.png"},
    "Product 4": {"price": 12.99, "image": "D:\Python\School\class12final\Screenshot 2023-05-17 184015.png"}
}

# List to store cart items
cart = []


# Function to add product to cart
def add_to_cart(product):
    cart.append(product)
    print(f"{product} added to cart. Current cart: {cart}")

def view_cart():
    cart_window = ctk.CTkToplevel(root)
    cart_window.title("Cart")
    cart_window.geometry("300x300")
    lbl = ctk.CTkLabel(cart_window, text=f"Cart: {cart}")
    lbl.grid(column=0, row=0)
    rowx = 1
    for procuct in cart:
        image = Image.open(details["image"])
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)

        image_label = ctk.CTkLabel(cart_window, text="", image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.grid(row=row, column=0, padx=10, pady=10)

        # Create a label to display the product name and price
        product_label = ctk.CTkLabel(cart_window, text=f"{product} - ${details['price']:.2f}")
        product_label.grid(row=row, column=1, padx=10, pady=10, sticky="w")

        qty_label = ctk.CTkLabel(cart_window, text=f"{cart.count(product)}")
        qty_label.grid(row=row, column=2, padx=10, pady=10, sticky="w")

        rowx += 1

# Create a label for the title
title_label = ctk.CTkLabel(root, text="Welcome to the E-Shop", font=("Arial", 20))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Display products row-wise with an image and "Add to Cart" button
row = 1
for product, details in products.items():
    # Load the product image
    image = Image.open(details["image"])
    image = image.resize((100, 100))
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = ctk.CTkLabel(root, text="", image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.grid(row=row, column=0, padx=10, pady=10)

    # Create a label to display the product name and price
    product_label = ctk.CTkLabel(root, text=f"{product} - ${details['price']:.2f}")
    product_label.grid(row=row, column=1, padx=10, pady=10, sticky="w")

    # Create an "Add to Cart" button
    add_button = ctk.CTkButton(root, text="Add to Cart", command=lambda p=product: add_to_cart(p))
    add_button.grid(row=row, column=2, padx=10, pady=10)

    row += 1

# Run the main event loop
view_cart = ctk.CTkButton(root, text="View Cart", command=view_cart)
view_cart.grid(row=row+1, column=0, padx=10, pady=10)
root.mainloop()
