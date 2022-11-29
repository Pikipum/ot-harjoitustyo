from user import User
from chat_message import Message
from ui.ui import UI
import tkinter
from tkinter import *
from tkinter import Tk, ttk
from functools import partial
from tkinter import messagebox


def main():
    window = tkinter.Tk()
    window.title("PyChat")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
