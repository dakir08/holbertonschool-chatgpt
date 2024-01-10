#!/usr/bin/python3
import unittest
from main import calculate_grade

import unittest

class TestCalculateGrade(unittest.TestCase):

    def test_not_yet_successful(self):
        self.assertEqual(calculate_grade(0), 'Not yet successful')
        self.assertEqual(calculate_grade(49), 'Not yet successful')

    def test_pass(self):
        self.assertEqual(calculate_grade(50), 'Pass')
        self.assertEqual(calculate_grade(60), 'Pass')

    def test_credit(self):
        self.assertEqual(calculate_grade(61), 'Credit')
        self.assertEqual(calculate_grade(75), 'Credit')

    def test_distinction(self):
        self.assertEqual(calculate_grade(76), 'Distinction')
        self.assertEqual(calculate_grade(85), 'Distinction')

    def test_high_distinction(self):
        self.assertEqual(calculate_grade(86), 'High Distinction')
        self.assertEqual(calculate_grade(100), 'High Distinction')

    def test_invalid_marks(self):
        with self.assertRaises(ValueError) as context:
            calculate_grade(-10)
        self.assertEqual(str(context.exception), "Mark must be in the range 0-100")

        with self.assertRaises(ValueError) as context:
            calculate_grade(105)
        self.assertEqual(str(context.exception), "Mark must be in the range 0-100")

if __name__ == '__main__':
    unittest.main()

