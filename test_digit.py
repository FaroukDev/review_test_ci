import unittest
from reverse_digit import reverse_digit

class TestStringMethods(unittest.TestCase):
    def test_ReverseTestCase(self):
        self.assertEqual(reverse_digit(321), 123)

if __name__ == '__main__':
    unittest.main()