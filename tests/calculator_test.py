import unittest
from src.calculator import add, subtract, divide, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_subtract(self):
        self.assertEqual(3, subtract(10, 7))

    def test_divide(self):
        self.assertEqual(2, divide(6, 3))

    def test_multiply(self):
        self.assertEqual(16, multiply(8, 2))       



        
    
