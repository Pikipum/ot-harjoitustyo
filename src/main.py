from user import User
from chat_message import Message
from ui import UI
import tkinter
from tkinter import *
from tkinter import Tk, ttk
from functools import partial
from tkinter import messagebox


# Users are stored in a dictionary. Their username is they key which returns the User object
users = {}

def main():
    window = tkinter.Tk()
    window.title("PyChat")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
