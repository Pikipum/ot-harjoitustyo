import tkinter
from functools import partial
from tkinter import Button, Entry, Label, StringVar, constants, ttk
from services import chat_services


class ChatScreen:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_message_field(self, input):
        message_label = ttk.Label(master=self._frame, text="Type message: ")

        message = input
        self._message_label_entry = ttk.Entry(
            master=self._frame, textvariable=message)

        message_label.grid(padx=5, pady=5, sticky=constants.W)
        self._message_label_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        message = StringVar()

        self._initialize_message_field(message)

        message_partial = partial(
            chat_services.send_message, message)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        send_button = tkinter.Button(
            master=self._frame, text="Send", command=message_partial)

        send_button.grid(padx=5, pady=5, sticky=constants.EW)
