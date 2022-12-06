import unittest
from services.chat_services import check_log_in, add_user, create_account, send_message, username_exists


class TestChatServices(unittest.TestCase):
    def setUp(self):
        add_user("name", "password")

    def test_check_login_works(self):
        self.assertEqual(check_log_in("name", "password"), True)

    def test_add_user(self):
        add_user("name2", "a")
        self.assertEqual(username_exists("name2"), True)

    def test_create_account(self):
        self.assertEqual(create_account("name3", "b"), False)

    def test_send_message(self):
        self.assertEqual(send_message("224565"), True)

    def test_username_exists(self):
        self.assertEqual(username_exists("name"), True)
