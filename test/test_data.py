import unittest
import sys
sys.path.append('path')
from factorial.fact import fact

class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = fact(5)
        self.assertEqual(res, 120)
        
        res = fact(6)
        self.assertEqual(res, 140)


if __name__ == '__main__':
    unittest.main()