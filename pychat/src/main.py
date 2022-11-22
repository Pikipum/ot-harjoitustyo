from user import User
from message import Message
from ui import UI
from tkinter import Tk, ttk
import tkMessageBox

window = Tk()
window.title("PyChat")

# Users are stored in a dictionary. Their username returns the User object
users = {}

# Create a new user and add it to the dictionary of users
def add_user(name, password):
    users[name: User(name, [], password)]

# Fetch user object from users dictionary, check if password is a match
def check_log_in(username, password):
    if password == users[username].get_password:
        tkMessageBox.showinfo( "Log in", "Log in succesful")
        return 1
    tkMessageBox.showinfo( "Log in", "Wrong password")
    return 0

log_in = Tk.Button(window, text ="Log in", command = check_log_in)

ui = UI(window)
ui.start()

window.mainloop()