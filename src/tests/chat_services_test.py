import unittest
from services.chat_services import chat_services


class TestChatServices(unittest.TestCase):
    def setUp(self):
        chat_services.add_user("name", "password")

    def test_check_login_works(self):
        self.assertEqual(chat_services.check_log_in("name", "password"), True)

    def test_add_user(self):
        chat_services.add_user("name2", "a")
        self.assertEqual(chat_services.username_exists("name2"), True)

    def test_create_account(self):
        self.assertEqual(chat_services.create_account("name3", "b"), False)

    def test_send_message(self):
        self.assertEqual(chat_services.send_message("224565"), True)

    def test_username_exists(self):
        self.assertEqual(chat_services.username_exists("name"), True)
