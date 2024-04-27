"""
    Sample test
"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """ Test the Calc modiul"""

    def test_add(self):
        """Test adding number together"""
        result = calc.add(5, 1)

        self.assertEqual(result, 6)
