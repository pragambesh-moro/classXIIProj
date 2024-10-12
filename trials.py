import customtkinter as ctk

# Sample data for cart items
cart_items = ["Product 1", "Product 2", "Product 3"]


def update_cart():
    # Clear the current cart display
    for widget in cart_frame.winfo_children():
        widget.destroy()

    # Display updated cart items
    for index, (item_name, item_details) in enumerate(cart_items.items()):
        img = Image.open(item_details["image"])
        img = img.resize((70, 70))
        img = ImageTk.PhotoImage(img)
        cart_window.images.append(img)  # Keep a reference to the image

        CTkLabel(cart_window, text=item_name).grid(row=index, column=0, padx=10, pady=10)
        CTkLabel(cart_window, text=item_details["quantity"]).grid(row=index, column=1, padx=10, pady=10)
        CTkLabel(cart_window, text=f"${float(item_details['price']) * float(item_details['quantity'])}").grid(row=index,
                                                                                                              column=2,
                                                                                                              padx=10,
                                                                                                              pady=10)
        CTkLabel(cart_window, text="", image=img).grid(row=index, column=3, padx=10, pady=10)
        tc += float(item_details['price']) * float(item_details['quantity'])
        CTkButton(cart_window, text='Delete', command=lambda item=item_name: delete_item(item)).grid(row=index,
                                                                                                     column=4, padx=10,
                                                                                                     pady=10)


def delete_item(item):
    # Remove the item from the cart
    cart_items.remove(item)
    # Update the cart display
    update_cart()


# Create the main window
root = ctk.CTk()
root.geometry("300x300")

# Create a frame for the cart items
cart_frame = ctk.CTkFrame(root)
cart_frame.pack(fill="both", expand=True)

# Initial cart display
update_cart()

# Run the application
root.mainloop()

