from tkinter import messagebox
from user import User

users = {}
messages = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]


class InvalidLoginError(Exception):
    pass


def username_exists(username):
    if username in users:
        return True
    return False

# Create a new user and add it to the dictionary of users


def add_user(name, password):
    users[name] = User(name, [], password)

# Fetch user object from users dictionary, check if password is a match


def check_log_in(username, password):
    if not isinstance(username, str):
        username = username.get()
        password = password.get()
    if not username_exists(username):
        #messagebox.showinfo("Log in", "Wrong username or password")
        return 0
    if password == users[username].password:
        #messagebox.showinfo("Log in", "Log in succesful")
        return 1
    return 0


# Check if username is already in users dictionary. If not, then add it.


def create_account(username, password):
    if not isinstance(username, str):
        username = username.get()
        password = password.get()
    if not username in users:
        add_user(username, password)
        #messagebox.showinfo(
        #    "Create account", "Account created succesfully")
        return 1
    #messagebox.showinfo("Create account", "Username already exists")
    return 0


def send_message(message):
    if not isinstance(message, str):
        message = message.get()
    messages.append(message)
    return 1


# Test user, username: admin, password: root
add_user("admin", "root")
