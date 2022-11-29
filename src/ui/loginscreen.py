import tkinter
from functools import partial
from tkinter import Button, Entry, Label, StringVar, constants, ttk
from services import chat_services
#from ui import UI


class LoginScreen:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_username_field(self, input):
        username_label = ttk.Label(master=self._frame, text="User name")

        username = input
        self._username_entry = ttk.Entry(
            master=self._frame, textvariable=username)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self, input):
        password_label = ttk.Label(master=self._frame, text="Password")

        password = input
        self._password_entry = ttk.Entry(
            master=self._frame, textvariable=password, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _login_handler(self, username, password):
        if chat_services.check_log_in(username, password) == 1:
            return None

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        password = StringVar()
        username = StringVar()

        self._initialize_username_field(username)
        self._initialize_password_field(password)

        check_log_in_partial = partial(
            self._login_handler, username, password)
        create_account_partial = partial(
            chat_services.create_account, username, password)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        log_in_button = tkinter.Button(
            master=self._frame, text="Log in", command=check_log_in_partial)
        create_account_button = tkinter.Button(
            master=self._frame, text="Create account", command=create_account_partial)

        log_in_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_account_button.grid(padx=5, pady=5, sticky=constants.EW)
