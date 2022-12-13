from functools import partial
from tkinter import Button, Entry, Label, StringVar, constants, Frame
from services.chat_services import chat_services


class ChatScreen:
    def __init__(self, root, current_user):
        self._root = root
        self._frame = None
        self.messages = chat_services._messages
        self._initialize()
        self.current_user = current_user

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_message_field(self, user_input):
        message_label = Label(master=self._frame, text="Type message: ")

        message_label_entry = Entry(
            master=self._frame, textvariable=user_input)

        message_label.grid(padx=5, pady=5, sticky=constants.W)
        message_label_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_message_history(self):
        offset = 2
        rows = 10

        message_count = len(self.messages)

        for i in range(1, rows):
            msg = self.messages.get(message_count-i)
            Label(self._frame, anchor=constants.W, text=msg).grid(
                row=i+offset, sticky=constants.W)

    def _refresh(self):
        self.destroy()
        self._initialize()
        self.pack()

    def _message_handler(self, msg):
        chat_services.send_message(msg)
        self._refresh()

    def _initialize(self):
        self._frame = Frame(master=self._root)

        message = StringVar()

        self._initialize_message_field(message)
        self._initialize_message_history()

        send_message_partial = partial(
            self._message_handler, message)

        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        send_button = Button(
            master=self._frame, text="Send", command=send_message_partial)

        send_button.grid(padx=5, pady=5, sticky=constants.EW)
