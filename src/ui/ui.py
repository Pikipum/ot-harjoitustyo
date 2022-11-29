from tkinter import Tk
from ui.loginscreen import LoginScreen
from ui.chatscreen import ChatScreen


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_screen()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_screen(self):
        self._hide_current_view()

        self._current_view = LoginScreen(self._root, self._show_chat_screen)

        self._current_view.pack()

    def _show_chat_screen(self, username):
        self._hide_current_view()
        self._current_view = ChatScreen(
            self._root,
            username)

        self._current_view.pack()
