from tkinter import messagebox
from user import User
from services.dataparser import get_accounts, get_messages, save_to_file, save_accounts


users = get_accounts()
messages = get_messages()
#messages = messages.get("MESSAGES")


class InvalidLoginError(Exception):
    pass


def username_exists(username):
    if username in users:
        return True
    return False

# Create a new user and add it to the dictionary of users


def add_user(name, password):
    users[name] = password

# Fetch user object from users dictionary, check if password is a match


def check_log_in(username, password):
    if not isinstance(username, str):
        username = username.get()
        password = password.get()
    if not username_exists(username):
        return 0
    if password == users.get(username):
        return 1
    return 0


# Check if username is already in users dictionary. If not, then add it.
def create_account(username, password):
    if not isinstance(username, str):
        username = username.get()
        password = password.get()
    if not username in users:
        add_user(username, password)
        save_accounts(users)
        return 1
    return 0


def send_message(message):
    if not isinstance(message, str):
        message = message.get()
    messages[len(messages)] = message
    save_to_file(messages)
    return 1
