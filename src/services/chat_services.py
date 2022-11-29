import tkinter
from user import User


users = {}

# Create a new user and add it to the dictionary of users
def add_user(name, password):
    users[name] = User(name, [], password)

# Fetch user object from users dictionary, check if password is a match


def check_log_in(username, password):
    username = username.get()
    password = password.get()
    if password == users[username].password:
        tkinter.messagebox.showinfo("Log in", "Log in succesful")
        return 1
    tkinter.messagebox.showinfo("Log in", "Wrong username or password")

# Check if username is already in users dictionary. If not, then add it.


def create_account(username, password):
    if not username.get() in users:
        add_user(username.get(), password.get())
        tkinter.messagebox.showinfo(
            "Create account", "Account created succesfully")
        return 1
    tkinter.messagebox.showinfo("Create account", "Username already exists")


# Test user, username: admin, password: root
add_user("admin", "root")
