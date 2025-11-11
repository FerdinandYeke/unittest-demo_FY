# tests/test_calculator.py

import unittest
from src.calculator import Calculator

class TestCalculatorBasics(unittest.TestCase):
    def setUp(self):
        # Runs before each test — creates a fresh Calculator instance
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        #pass    
