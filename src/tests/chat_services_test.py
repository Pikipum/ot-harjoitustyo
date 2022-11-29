import unittest
from tkinter import StringVar, Entry
#from user import User
from services.chat_services import check_log_in, add_user, create_account, send_message, username_exists


class TestChatServices(unittest.TestCase):
    def setUp(self):
        add_user("name", "password")
        self.name = StringVar()
        self.password = StringVar()

        self.name_entry = Entry(self, textvariable=self.name)
        self.password_entry = Entry(self, textvariable=self.password)

    def test_check_login_works(self):

        self.assertEqual(check_log_in(self.name_entry, self.password_entry), True)

    def test_add_user(self):
        self.assertEqual(str(chat_services.add_user), True)

    def test_create_account(self):
        self.assertEqual(str(chat_services.create_account), True)

    def test_send_message(self):
        self.assertEqual(str(chat_services.send_message), True)

    def test_username_exists(self):
        self.assertEqual(str(chat_services.username_exists), True)
