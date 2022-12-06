import unittest
from chat_message import Message


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message = Message("1", "abcd", "1", "1")

    def test_chat_message_exists(self):
        self.assertEqual(str(self.message), "1")

    def test_chat_message_is_correct(self):
        self.assertEqual(str(self.message.msg), "abcd")

    def test_chat_message_id_is_correct(self):
        self.assertEqual(str(self.message.msg), "abcd")

    def test_time_is_correct(self):
        self.assertEqual(str(self.message.time), "1")

    def test_user_is_correct(self):
        self.assertEqual(str(self.message.user), "1")
