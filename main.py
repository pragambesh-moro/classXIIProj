"""Class 12 project"""

# IMPORTS
import mysql.connector as mc
from customtkinter import *
from PIL import Image, ImageTk

# MYSQL CONNECTION
mycon = mc.connect(host="localhost", user="root", password="batszeus", database="retailplatform", connection_timeout=600)
mycur = mycon.cursor()
if mycon.is_connected():
    print("Connected to MySQL")
    mycur.execute("SELECT VERSION()")
    data = mycur.fetchone()
    print("MySQL Version:", data)

products = {
    "Product 1": {"price": 10.99, "image":"Screenshot 2023-05-17 184015.png"},
    "Product 2": {"price": 15.49, "image": "Screenshot 2023-05-17 221145.png"},
    "Product 3": {"price": 7.99, "image": "Screenshot 2023-05-17 221153.png"},
    "Product 4": {"price": 12.99, "image": "Screenshot 2023-05-20 092017.png"}
}
cart_items = {}

def add_to_cart(item_name):
    if item_name in products:
        if item_name in cart_items:
            cart_items[item_name]["quantity"] += 1
        else:
            cart_items[item_name] = {
                "quantity": 1,
                "price": products[item_name]["price"],
                "image": products[item_name]["image"]
            }
        print(f"Added {item_name} to cart.")
    else:
        print(f"Item {item_name} not found in products.")
# Functions
def app_quitter():
    mycon.commit()
    mycur.close()
    mycon.close()
    app.quit()


def singup_final():
    un = user_name.get()
    ui = user_id.get()
    upwdd = user_pwd.get()
    uemail = user_email.get()
    uaddress = user_address.get()
    uph = int(user_ph.get())

    qry = f"insert into user_details values('{ui}', '{un}', '{uemail}', {uph}, '{upwdd}', '{uaddress}')"

    mycur.execute(qry)
    mycon.commit()

    scs = CTkLabel(signup_win, text="Submitted Successfully")
    scs.pack(padx=10, pady=10)

def open_cart_window():
    global cart_window
    cart_window = CTkToplevel(app)
    cart_window.title("Cart")
    cart_window.geometry("600x400")

    for index, (item_name, item_details) in enumerate(cart_items.items()):
        img = Image.open(item_details["image"])
        img = img.resize((50, 50))
        img = ImageTk.PhotoImage(img)

        CTkLabel(cart_window, text=item_name).grid(row=index, column=0, padx=10, pady=10)
        CTkLabel(cart_window, text=item_details["quantity"]).grid(row=index, column=1, padx=10, pady=10)
        CTkLabel(cart_window, text=f"${float(item_details['price']) * float(item_details['quantity'])}").grid(row=index, column=2, padx=10, pady=10)
        CTkLabel(cart_window, text="", image=img).grid(row=index, column=3, padx=10, pady=10)
            # Keep a reference to the image to prevent garbage collection
        cart_window.image = img
    CTkLabel(cart_window, text="").grid(row=index, column=0, padx=10, pady=10)

def signin_final():
    ui = uid.get()
    upw = upwd.get()
    qry = f"SELECT * FROM user_details WHERE uid = '{ui}' AND upwd = '{upw}'"
    mycur.execute(qry)
    data = mycur.fetchall()
    print(data)
    if data:
        scs = CTkLabel(signin_win, text="Logged-In Successfully")
        scs.pack(padx=10, pady=10)
    else:
        fail = CTkLabel(signin_win, text="Username or Password is incorrect")
        fail.pack(padx=10, pady=10)
    if scs:
        signin_win.destroy()
        global main_window
        main_window = CTkToplevel(app)
        main_window.title("Shop")
        main_window.geometry("800x600")
        title_label = CTkLabel(main_window, text="Welcome to the E-Shop", font=("Arial", 20))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        row = 1
        for product, details in products.items():
            # Load the product image
            image = Image.open(details["image"])
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)

            # Create a label to display the image
            image_label = CTkLabel(main_window, text="", image=photo)
            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.grid(row=row, column=0, padx=10, pady=10)

            # Create a label to display the product name and price
            product_label = CTkLabel(main_window, text=f"{product} - ${details['price']:.2f}")
            product_label.grid(row=row, column=1, padx=10, pady=10, sticky="w")

            # Create an "Add to Cart" button
            add_button = CTkButton(main_window, text="Add to Cart", command=lambda p=product: add_to_cart(p))
            add_button.grid(row=row, column=2, padx=10, pady=10)

            row += 1


        view_cart = CTkButton(main_window, text="View Cart", command=open_cart_window)
        view_cart.grid(row=row + 1, column=0, padx=10, pady=10)

        logoutbt = CTkButton(main_window, text="Logout", command=logout)
        logoutbt.grid(row = row + 1, column=1, padx=10, pady=10)




def logout():
    main_window.destroy()
    signin()
# CTK
app = CTk()
set_appearance_mode("dark")
app.title("Retail Platform")
app.geometry("500x150")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
def signup():
    global signup_win
    signup_win = CTkToplevel(app)
    signup_win.title("Sign Up")
    signup_win.geometry("500x500")
    global user_name, user_id, user_pwd, user_email, user_address, user_ph

    user_name = CTkEntry(signup_win, placeholder_text="Enter Name")
    user_name.pack(padx=10, pady=10)

    user_id = CTkEntry(signup_win, placeholder_text="Enter ID")
    user_id.pack(padx=10, pady=10)

    user_email = CTkEntry(signup_win, placeholder_text="Enter E-mail")
    user_email.pack(padx=10, pady=10)

    user_address = CTkEntry(signup_win, placeholder_text="Enter address")
    user_address.pack(padx=10, pady=10)

    user_ph = CTkEntry(signup_win, placeholder_text="Enter Phone Number")
    user_ph.pack(padx=10, pady=10)

    user_pwd = CTkEntry(signup_win, placeholder_text="Enter Password", show='*')
    user_pwd.pack(padx=10, pady=10)

    btn = CTkButton(master=signup_win, text="SUBMIT", command=singup_final)
    btn.pack(padx=10, pady=10)

    btn = CTkButton(master=signup_win, text="QUIT", command=app_quitter)
    btn.pack(padx=10, pady=10)

def signin():
    global signin_win
    signin_win = CTkToplevel(app)
    signin_win.title("Sign In")
    signin_win.geometry("300x300")
    signin_win.focus_set()
    global uid, upwd

    uid = CTkEntry(signin_win, placeholder_text="Enter ID")
    uid.pack(padx=10, pady=10)

    upwd = CTkEntry(signin_win, placeholder_text="Enter Password", show='*')
    upwd.pack(padx=10, pady=10)

    btxt = CTkButton(signin_win, text="Login", command=signin_final)
    btxt.pack(padx=10, pady=10)

lbl = CTkLabel(app, text="Welcome to Retail Platform")
lbl.grid(row=0, column=0, columnspan=3, pady=10)

button = CTkButton(app, text="Sign Up", command=signup)
button.grid(row=3, column=0, pady=20, padx=20)

button2 = CTkButton(app, text="Sign In", command=signin)
button2.grid(row=3, column=1, pady=20, padx=20)

button3 = CTkButton(app, text="Quit", command=app_quitter)
button3.grid(row=3, column=2, pady=20, padx=20)


app.mainloop()
mycon.close()
if mycon.is_connected():
    print("still connected")
else:
    print("Not connected")
