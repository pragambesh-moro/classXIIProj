import customtkinter as ctk

def on_button1_click():
    print("Button 1 clicked")
    messagebox_window.destroy()  # Close the message box

def on_button2_click():
    print("Button 2 clicked")
    messagebox_window.destroy()  # Close the message box

def create_ctk_messagebox(message):
    global messagebox_window
    messagebox_window = ctk.CTkToplevel()
    messagebox_window.title("Message Box")
    messagebox_window.geometry("300x150")

    # Message label
    message_label = ctk.CTkLabel(messagebox_window, text=message)
    message_label.pack(pady=20)

    # Frame to hold the buttons
    button_frame = ctk.CTkFrame(messagebox_window)
    button_frame.pack(pady=10)

    # Two buttons side by side
    button1 = ctk.CTkButton(button_frame, text="Button 1", command=on_button1_click)
    button1.grid(row=0, column=0, padx=10)

    button2 = ctk.CTkButton(button_frame, text="Button 2", command=on_button2_click)
    button2.grid(row=0, column=1, padx=10)

    messagebox_window.mainloop()

# Example usage
create_ctk_messagebox("Do you want to proceed?")

