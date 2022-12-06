import unittest
from user import User


class TestUser(unittest.TestCase):
    # Users have a name and a list of messages they have sent
    def setUp(self):
        self.user = User("name", [], "password")

    def test_user_exists(self):
        self.assertEqual(str(self.user), "name")
