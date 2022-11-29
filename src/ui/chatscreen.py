import tkinter
from functools import partial
from tkinter import Button, Entry, Label, StringVar, constants, ttk
from services import chat_services


class ChatScreen:
    def __init__(self, root, current_user):
        self._root = root
        self._frame = None
        self.messages = chat_services.messages
        self.r = 0
        self._initialize()
        self.current_user = current_user

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

    def _initialize_message_history(self):
        offset = 2
        rows = 10

        for i in range(1, rows):
            msg = self.messages[-i]
            tkinter.Label(self._frame, anchor=tkinter.W, text=msg).grid(
                row=i+offset, sticky=tkinter.W)

    def refresh(self):
        self.destroy()
        self._initialize()
        self.pack()

    def _message_handler(self, msg):
        chat_services.send_message(msg)
        self.refresh()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        message = StringVar()

        self._initialize_message_field(message)
        self._initialize_message_history()

        send_message_partial = partial(
            self._message_handler, message)

        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        send_button = tkinter.Button(
            master=self._frame, text="Send", command=send_message_partial)

        send_button.grid(padx=5, pady=5, sticky=constants.EW)
