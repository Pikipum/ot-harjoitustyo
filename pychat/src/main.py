from user import User
from message import Message
from ui import UI
from tkinter import Tk, ttk

window = Tk()
window.title("PyChat")

ui = UI(window)
ui.start()

window.mainloop()