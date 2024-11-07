"""Class 12 project"""
import eggs
# IMPORTS
from eggs import *
import mysql.connector as mc
from customtkinter import *
from PIL import Image, ImageTk

# MYSQL CONNECTION
mycon = mc.connect(host="localhost", user="root", password="sql123", database="retailplatform", connection_timeout=600)
mycur = mycon.cursor()
if mycon.is_connected():
    print("Connected to MySQL")
    mycur.execute("SELECT VERSION()")
    data = mycur.fetchone()
    print("MySQL Version:", data)

products = {
    "Product 1": {"price": 10.99, "image": "Screenshot 2023-05-17 184015.png"},
    "Product 2": {"price": 15.49, "image": "Screenshot 2023-05-17 221145.png"},
    "Product 3": {"price": 7.99, "image": "Screenshot 2023-05-17 221153.png"},
    "Product 4": {"price": 12.99, "image": "Screenshot 2023-05-20 092017.png"}
}
cart_items = {}
item_widgets = {}


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
    ubal = 10000.0
    uph = int(user_ph.get())

    qry = f"insert into user_details values('{ui}', '{un}', '{uemail}', {uph}, '{upwdd}', '{uaddress}', {ubal})"

    mycur.execute(qry)
    mycon.commit()

    scs = CTkLabel(signup_win, text="Submitted Successfully")
    scs.pack(padx=10, pady=10)


def update_cart_display():
    global total_cost
    total_cost = 0
    for item_name, widgets in item_widgets.items():
        item_info = cart_items[item_name]
        widgets['quantity_label'].configure(text=f"Quantity: {item_info['quantity']}")
        widgets['price_label'].configure(text=f"Price: {item_info['price']}")
        widgets['image_label'].configure(image=CTkImage(light_image=Image.open(item_info['image']), size=(70, 70)))
        total_cost += float(item_info['price']) * float(item_info['quantity'])
        total_cost
        total_cost_label.configure(text=f"Total cost: ${total_cost}")


def delete_itms(item_name):
    cart_items[item_name]["quantity"] -= 1
    print(f"Deleted {item_name} from cart.")
    if cart_items[item_name]["quantity"] == 0:
        # Remove the item from the cart
        del cart_items[item_name]
        item_widgets[item_name]['quantity_label'].grid_forget()
        item_widgets[item_name]['price_label'].grid_forget()
        item_widgets[item_name]['image_label'].grid_forget()
        item_widgets[item_name]['name_label'].grid_forget()
        item_widgets[item_name]['delete_button'].grid_forget()
        del item_widgets[item_name]
    if not cart_items:
        total_cost_label.grid_forget()
        empty_lbl = CTkLabel(cart_window, text="Your Cart is Empty!!", font=("Arial", 20))
        empty_lbl.grid(row=0, column=0, columnspan=3, pady=10)
    update_cart_display()


def pay():
    global dialog, usn_entry, pwd_entry
    dialog = CTkToplevel(app)
    dialog.title("Payment Page")
    dialog.geometry("400x200")

    payment_lbl = CTkLabel(dialog, text=f"Payment due is ${total_cost}")
    payment_lbl.pack(pady=20)

    usn_entry = CTkEntry(dialog, placeholder_text="Enter Username")
    usn_entry.pack(pady=20)

    pwd_entry = CTkEntry(dialog, placeholder_text="Enter Password", show='*')
    pwd_entry.pack(pady=20)

    subt_btn = CTkButton(dialog, text="Submit", command=fin_pay)
    subt_btn.pack(pady=20)


def fin_pay():
    global cart_items, item_widgets
    print(usn_entry.get())
    print(pwd_entry.get())
    print(ui)
    print(upw)
    if usn_entry.get() == ui and pwd_entry.get() == upw:
        qry2 = f"SELECT Balance from user_details where uid like '{ui}%'"
        mycur.execute(qry2)
        bal = mycur.fetchone()
        print(f"Payment of ${total_cost} was succesful")
        paid_cost = bal[0] - total_cost
        qry3 = f"update user_details set Balance = {paid_cost} where uid like '{ui}%'"
        eggs.gen_bill()
        mycur.execute(qry3)
        mycon.commit()
        cart_items = {}
        item_widgets = {}
        dialog.destroy()
        messagebox_window.destroy()
        cart_window.destroy()

    else:
        print("Something Went Wrong")


def check_out():
    global messagebox_window, total_cost
    messagebox_window = CTkToplevel(app)
    messagebox_window.title("Check Out")
    messagebox_window.geometry("500x150")
    if total_cost:
        if total_cost != 0 and total_cost <= tc:
            tx = total_cost
        checkout_lbl = CTkLabel(messagebox_window, text=f"Payment due: ${tx}")
        checkout_lbl.grid(row=0, column=1, pady=10)
    else:
        checkout_lbl = CTkLabel(messagebox_window, text=f"Payment due: ${tc}")
        checkout_lbl.grid(row=0, column=1, pady=10)
    button_pay = CTkButton(messagebox_window, text="Pay", command=pay)
    button_pay.grid(row=3, column=0, pady=20, padx=20)

    button_cancel = CTkButton(messagebox_window, text="Cancel", command=(messagebox_window.destroy))
    button_cancel.grid(row=3, column=1, pady=20, padx=20)


def open_cart_window():
    global cart_window, item_name, total_cost_label, tc, toal_cost
    cart_window = CTkToplevel(app)
    cart_window.title("Cart")
    cart_window.geometry("700x700")
    cart_window.images = []  # Store images here to prevent garbage collection
    tc = 0

    if cart_items:
        for index, (item_name, item_details) in enumerate(cart_items.items()):
            img = Image.open(item_details["image"])
            img = img.resize((70, 70))
            img = ImageTk.PhotoImage(img)
            cart_window.images.append(img)  # Keep a reference to the image

            name_lbl = CTkLabel(cart_window, text=item_name)
            name_lbl.grid(row=index, column=0, padx=10, pady=10)
            qty_lbl = CTkLabel(cart_window, text=f" Quantity: {item_details['quantity']}")
            qty_lbl.grid(row=index, column=1, padx=10, pady=10)
            pri_lbl = CTkLabel(cart_window,
                               text=f"Price: ${float(item_details['price']) * float(item_details['quantity'])}")
            pri_lbl.grid(row=index, column=2, padx=10, pady=10)
            img_lbl = CTkLabel(cart_window, text="", image=img)
            img_lbl.grid(row=index, column=3, padx=10, pady=10)
            tc += float(item_details['price']) * float(item_details['quantity'])
            del_but = CTkButton(cart_window, text='Delete', command=lambda item=item_name: delete_itms(item))
            del_but.grid(row=index, column=4, padx=10, pady=10)
            global total_cost
            total_cost = tc

            item_widgets[item_name] = {
                'name_label': name_lbl,
                'quantity_label': qty_lbl,
                'price_label': pri_lbl,
                'image_label': img_lbl,
                'delete_button': del_but
            }

        checkout_btn = CTkButton(cart_window, text='Checkout', command=check_out)
        checkout_btn.grid(row=index + 1, column=1, padx=10, pady=10)
        total_cost_label = CTkLabel(cart_window, text=f"Total cost: {tc}")
        total_cost_label.grid(row=index + 1, column=0, padx=10, pady=10)

    else:
        # total_cost_label.grid_forget()
        empty_lbl = CTkLabel(cart_window, text="Your Cart is Empty!!", font=("Arial", 20))
        empty_lbl.grid(row=0, column=0, columnspan=3, pady=10)

    CTkLabel(cart_window, text="").grid(row=index, column=0, padx=10, pady=10)


def signin_final():
    global ui, upw, uxname
    ui = uid.get()
    upw = upwd.get()
    qry = f"SELECT * FROM user_details WHERE uid = '{ui}' AND upwd = '{upw}'"
    mycur.execute(qry)
    data = mycur.fetchall()
    print(data)
    qn = f"SELECT uname FROM user_details WHERE uid = '{ui}' AND upwd = '{upw}'"
    mycur.execute(qn)
    uxname = (mycur.fetchone())[0]
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
        logoutbt.grid(row=row + 1, column=1, padx=10, pady=10)


def logout():
    global cart_items, item_widgets
    cart_items = {}
    item_widgets = {}
    main_window.destroy()
    cart_window.destroy()
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

global ui, uxname, total_cost

app.mainloop()
mycon.close()
if mycon.is_connected():
    print("still connected")
else:
    print("Not connected")