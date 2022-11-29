import tkinter
from user import User
#from ui.ui import UI


users = {}
messages = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]


def username_exists(username):
    if username in users:
        return True
    return False

# Create a new user and add it to the dictionary of users


def add_user(name, password):
    users[name] = User(name, [], password)

# Fetch user object from users dictionary, check if password is a match


def check_log_in(username, password):
    username = username.get()
    password = password.get()
    if not username_exists(username):
        tkinter.messagebox.showinfo("Log in", "Wrong username or password")
        return 0
    if password == users[username].password:
        tkinter.messagebox.showinfo("Log in", "Log in succesful")
        return 1


# Check if username is already in users dictionary. If not, then add it.


def create_account(username, password):
    if not username.get() in users:
        add_user(username.get(), password.get())
        tkinter.messagebox.showinfo(
            "Create account", "Account created succesfully")
        return 1
    tkinter.messagebox.showinfo("Create account", "Username already exists")


def send_message(message):
    messages.append(message.get())


# Test user, username: admin, password: root
add_user("admin", "root")
