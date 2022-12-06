from functools import partial
from tkinter import Button, Entry, Label, StringVar, constants, messagebox, Frame
from services.chat_services import check_log_in, create_account


class LoginScreen:
    def __init__(self, root, handle_login):
        self._root = root
        self._frame = None
        self._handle_login = handle_login

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_username_field(self, user_input):
        username_label = Label(master=self._frame, text="User name")
        username_entry = Entry(
            master=self._frame, textvariable=user_input)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self, user_input):
        password_label = Label(master=self._frame, text="Password")

        password_entry = Entry(
            master=self._frame, textvariable=user_input, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _login_handler(self, username, password):
        if check_log_in(username, password):
            self._handle_login(username.get())
        else:
            messagebox.showinfo("Error", "Wrong username or password")

    def _account_create_handler(self, username, password):
        if create_account(username, password):
            messagebox.showinfo("Success", "Account created")
        else:
            messagebox.showinfo("Error", "Username already taken")

    def _initialize(self):
        self._frame = Frame(master=self._root)

        password = StringVar()
        username = StringVar()

        self._initialize_username_field(username)
        self._initialize_password_field(password)

        check_log_in_partial = partial(
            self._login_handler, username, password)
        create_account_partial = partial(
            self._account_create_handler, username, password)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        log_in_button = Button(
            master=self._frame, text="Log in", command=check_log_in_partial)
        create_account_button = Button(
            master=self._frame, text="Create account", command=create_account_partial)

        log_in_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_account_button.grid(padx=5, pady=5, sticky=constants.EW)
