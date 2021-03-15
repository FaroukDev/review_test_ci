import unittest
from number_of_word import number_of_word

class TestStringMethods(unittest.TestCase):
    def test_ReverseTestCase(self):
        self.assertEqual(number_of_word("Hello les devclouds"), 3)

if __name__ == '__main__':
    unittest.main()