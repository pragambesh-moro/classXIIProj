import tkinter as tk
import mysql.connector as mc

# MYSQL CONNECTION
mycon = mc.connect(host="localhost", user="root", password="batszeus", database="retailplatform")
mycur = mycon.cursor()
if mycon.is_connected():
    print("Connected to MySQL")
    mycur.execute("SELECT VERSION()")
    data = mycur.fetchone()
    print("MySQL Version:", data)

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


root = tk.Tk()
root.title("Test")
root.geometry("500x500")
user_name = PlaceholderEntry(root, placeholder="Enter Name")
user_name.pack(padx=10, pady=10)

user_id = PlaceholderEntry(root, placeholder="Enter ID")
user_id.pack(padx=10, pady=10)

user_email = PlaceholderEntry(root, placeholder="Enter E-mail")
user_email.pack(padx=10, pady=10)

user_address = PlaceholderEntry(root, placeholder="Enter address")
user_address.pack(padx=10, pady=10)

user_ph = PlaceholderEntry(root, placeholder="Enter Phone Number")
user_ph.pack(padx=10, pady=10)

user_pwd = PlaceholderEntry(root, placeholder="Enter Password", show='*')
user_pwd.pack(padx=10, pady=10)
#
# btn = CTkButton(master=root, text="SUBMIT", command=OnButtonClick)
# btn.pack(padx=10, pady=10)
#
# btn = CTkButton(master=root, text="QUIT", command=app_quitter)
# btn.pack(padx=10, pady=10)
root.mainloop()