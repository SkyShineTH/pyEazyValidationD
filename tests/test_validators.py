import unittest
from datavalidator.validators import *

class TestValidators(unittest.TestCase):

    def test_validate_type(self):
        validate_type(123, int)
        with self.assertRaises(ValidationError):
            validate_type("123", int)

    def test_validate_length(self):
        validate_length("hello", min_length=3)
        validate_length("hello", max_length=10)
        with self.assertRaises(ValidationError):
            validate_length("hi", min_length=3)
        with self.assertRaises(ValidationError):
            validate_length("hello world", max_length=5)

    def test_validate_regex(self):
        validate_regex("example@mail.com", r'^\S+@\S+\.\S+$')
        with self.assertRaises(ValidationError):
            validate_regex("example.com", r'^\S+@\S+\.\S+$')

    def test_validate_range(self):
        validate_range(10, min_value=5, max_value=15)
        with self.assertRaises(ValidationError):
            validate_range(4, min_value=5)
        with self.assertRaises(ValidationError):
            validate_range(16, max_value=15)

if __name__ == '__main__':
    unittest.main()