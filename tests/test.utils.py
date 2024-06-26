import unittest
from datavalidator.utils import *

class TestUtils(unittest.TestCase):

    def test_is_integer(self):
        self.assertTrue(is_integer(123))
        self.assertFalse(is_integer("123"))

    def test_is_float(self):
        self.assertTrue(is_float(123.45))
        self.assertFalse(is_float(123))

    def test_is_string(self):
        self.assertTrue(is_string("hello"))
        self.assertFalse(is_string(123))

    def test_matches_regex(self):
        self.assertTrue(matches_regex("example@mail.com", r'^\S+@\S+\.\S+$'))
        self.assertFalse(matches_regex("example.com", r'^\S+@\S+\.\S+$'))

if __name__ == '__main__':
    unittest.main()