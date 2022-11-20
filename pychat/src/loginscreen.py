from tkinter import ttk, constants

class LoginScreen:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Log in:")

        button = ttk.Button(
            master=self._frame,
            text="Enter username and password",
            command=self._handle_hello
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)