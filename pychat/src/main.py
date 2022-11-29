from user import User
from chat_message import Message
from ui import UI
import tkinter
from tkinter import *
from tkinter import Tk, ttk
from functools import partial
from tkinter import messagebox

window = tkinter.Tk()
window.title("PyChat")

# Users are stored in a dictionary. Their username is they key which returns the User object
users = {}

# Create a new user and add it to the dictionary of users
def add_user(name, password):
    users[name] = User(name, [], password)

# Fetch user object from users dictionary, check if password is a match
def check_log_in(username, password):
    username = username.get()
    password = password.get()
    if password == users[username].password:
        tkinter.messagebox.showinfo( "Log in", "Log in succesful")
        return 1
    tkinter.messagebox.showinfo( "Log in", "Wrong username or password")

# Check if username is already in users dictionary. If not, then add it.
def create_account(username, password):
    if not username.get() in users:
        add_user(username.get(), password.get())
        tkinter.messagebox.showinfo( "Create account", "Account created succesfully")
        return 1
    tkinter.messagebox.showinfo( "Create account", "Username already exists")

# Box to type in username
usernameLabel = Label(window, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(window, textvariable=username).grid(row=0, column=1)  

# Box to type in password
pwLabel = Label(window, text="Password").grid(row=1, column=0)
pw = StringVar()
pwEntry = Entry(window, textvariable=pw, show="*").grid(row=1, column=1)  

check_log_in = partial(check_log_in, username, pw)
create_account = partial(create_account, username, pw)

log_in_button = tkinter.Button(window, text ="Log in", command = check_log_in).grid(row=4, column=0) 
create_account_button = tkinter.Button(window, text ="Create account", command = create_account).grid(row=4, column=1) 

# Test user, username: admin, password: root
add_user("admin", "root")

window.mainloop()