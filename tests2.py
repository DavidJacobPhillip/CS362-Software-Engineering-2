# author: Santosh Ramesh

# imports
import random
import string
import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
    def test1(self):
        # Checking if empty password is accepted
        input = ""
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        # Checking if an 8-digit character is accepted
        input = "ABcd12~="
        expected = True
        self.assertEqual(check_pwd(input), expected)
    
    def test3(self):
        # Checking if an 21-digit character is accepted
        input = "ABcd12~=ABcd12~=ABcd1"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test4(self):
        # Checking if password with only digits is accepted (8 characters)
        input = "12345678"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test5(self):
        # Checking if password with only lowercase is accepted (8 characters)
        input = "abcdefgh"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test6(self):
        # Checking if password with only characters are accepted (8 characters)
        input = "abcdEFGH"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test7(self):
        # Checking if password with only characters or digits are accepted (12 characters)
        input = "abcdEFGH1234"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test8(self):
        # Checking if password with only characters or digits are accepted (12 characters)
        input = "abcdeFGHIJ12345~`!@#"
        expected = True
        self.assertEqual(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()
