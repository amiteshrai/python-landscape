""" Testing Calc Module """

import unittest

import src.unit_testing.calc as calc
from src.utils.logger import get_logger

LOGGER = get_logger(__name__)


class TestCalc(unittest.TestCase):
    """ TestCalc Class """

    def test_add(self):
        """ Test add function """

        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(2, -2), 0)

    def test_subtract(self):
        """ Test subtract function """

        self.assertEqual(calc.subtract(2, 3), -1)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(2, -2), 4)

    def test_divide(self):
        """ Test divide function """

        self.assertEqual(calc.divide(2, 3), 0)
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(2, -2), -1)

        # self.assertEqual(calc.divide(2, 0), None)  # Failure

        # Testing For Exceptions
        self.assertRaises(ValueError, calc.divide, 2, 0)

        # Testing For Exceptions using context manager
        with self.assertRaises(ValueError):
            calc.divide(2, 0)

        # self.assertEqual(calc.divide(2, None), None)  # Failure
        # self.assertEqual(calc.divide(None, None), None)  # Failure
        self.assertEqual(calc.divide(5, 2), 2)
        # self.assertEqual(calc.divide(5, 2), 2.5)  # Failure


# When this module is run directly, run all the test cases
# However, there is some issue with VS Code which result in error
if __name__ == "__main__":
    unittest.main()
