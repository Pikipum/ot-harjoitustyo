import unittest
from chat_message import Message

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message = Message("1", "abcd", "1", "1")

    def test_chat_message_exists(self):
        self.assertEqual(str(self.message), "abcd")