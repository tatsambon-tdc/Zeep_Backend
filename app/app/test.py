"""
Sample test
"""

from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """ Test the Calc modiul"""
    
    def  test_add(self):
        """Test adding number together"""
        res = calc.add(5, 1)
         
        self.assertEqual(res, 6)
