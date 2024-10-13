import customtkinter as ctk
from PIL import Image

# Sample data for the cart
cart_items = {
    'item1': {'name': 'Apple', 'quantity': 5, 'price': 10, 'image': 'Screenshot 2023-05-17 184015.png'},
    'item2': {'name': 'Banana', 'quantity': 3, 'price': 5, 'image': 'Screenshot 2023-05-17 184015.png'}
}


# Function to update the quantity and refresh the display
def decrement_quantity(item_key):
    if cart_items[item_key]['quantity'] > 0:
        cart_items[item_key]['quantity'] -= 1
        update_cart_display()


# Function to update the cart display
def update_cart_display():
    for item_key, widgets in item_widgets.items():
        item_info = cart_items[item_key]
        widgets['quantity_label'].configure(text=f"Quantity: {item_info['quantity']}")
        widgets['price_label'].configure(text=f"Price: {item_info['price']}")
        widgets['image_label'].configure(image=ctk.CTkImage(light_image=Image.open(item_info['image']), size=(50, 50)))


root = ctk.CTk()
root.geometry("500x400")

item_widgets = {}

# Create the cart display
for idx, (item_key, item_info) in enumerate(cart_items.items()):
    name_label = ctk.CTkLabel(root, text=item_info['name'])
    name_label.grid(row=idx, column=0, padx=10, pady=5)

    quantity_label = ctk.CTkLabel(root, text=f"Quantity: {item_info['quantity']}")
    quantity_label.grid(row=idx, column=1, padx=10, pady=5)

    price_label = ctk.CTkLabel(root, text=f"Price: {item_info['price']}")
    price_label.grid(row=idx, column=2, padx=10, pady=5)

    image = ctk.CTkImage(light_image=Image.open(item_info['image']), size=(50, 50))
    image_label = ctk.CTkLabel(root, image=image, text="")
    image_label.grid(row=idx, column=3, padx=10, pady=5)

    decrement_button = ctk.CTkButton(root, text="-", command=lambda key=item_key: decrement_quantity(key))
    decrement_button.grid(row=idx, column=4, padx=10, pady=5)

    item_widgets[item_key] = {
        'quantity_label': quantity_label,
        'price_label': price_label,
        'image_label': image_label
    }

root.mainloop()
