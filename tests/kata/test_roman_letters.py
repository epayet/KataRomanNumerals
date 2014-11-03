__author__ = 'manu'

import unittest
from roman_letters import to_roman


class RomanLettersTestCase(unittest.TestCase):
    def test_one(self):
        roman = to_roman(1)
        self.assertEqual(roman, "I")

    def test_two(self):
        roman = to_roman(2)
        self.assertEqual(roman, "II")


if __name__ == '__main__':
    unittest.main()
