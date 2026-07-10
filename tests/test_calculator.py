import unittest
from app.calculator import divide, add, subtract, multiply, power

FIVE = 5

class TestCalculator(unittest.TestCase):
    def test_divide(self) -> None:
        """
        Test the divide function.

        This function tests the divide function from the calculator module.
        It checks if the result of dividing 10 by 2 is equal to 5.
        """
        self.assertEqual(divide(10, 2), FIVE)

    def test_add(self) -> None:
        """
        Test the add function.

        This function tests the add function from the calculator module.
        It checks if the result of adding 2 and 3 is equal to 5.
        """
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        """
        Test the subtract function.

        This function tests the subtract function from the calculator module.
        It checks if the result of subtracting 2 from 5 is equal to 3.
        """
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self) -> None:
        """
        Test the multiply function.

        This function tests the multiply function from the calculator module.
        It checks if the result of multiplying 3 and 4 is equal to 12.
        """
        self.assertEqual(multiply(3, 4), 12)

    def test_power(self) -> None:
        """
        Test the power function.

        This function tests the power function from the calculator module.
        It checks if the result of 2 to the power of 3 is equal to 8.
        """
        self.assertEqual(power(2, 3), 8)

if __name__ == '__main__':
    unittest.main()