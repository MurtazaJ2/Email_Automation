import unittest
from app.calculator import add, subtract, multiply, power, divide

class TestCalculator(unittest.TestCase):
    def test_divide(self) -> None:
        """Test the divide function with two positive numbers.
        
        This function tests the divide function from the calculator module.
        It checks if the division of 10 by 2 equals 5.
        
        Args:
        None
        
        Returns:
        None
        """
        self.assertEqual(divide(10, 2), 5)

    def test_add(self) -> None:
        """Test the add function with two positive numbers.
        
        This function tests the add function from the calculator module.
        It checks if the sum of 2 and 3 equals 5.
        
        Args:
        None
        
        Returns:
        None
        """
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        """Test the subtract function with two positive numbers.
        
        This function tests the subtract function from the calculator module.
        It checks if the difference of 5 and 2 equals 3.
        
        Args:
        None
        
        Returns:
        None
        """
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self) -> None:
        """Test the multiply function with two positive numbers.
        
        This function tests the multiply function from the calculator module.
        It checks if the product of 3 and 4 equals 12.
        
        Args:
        None
        
        Returns:
        None
        """
        self.assertEqual(multiply(3, 4), 12)

    def test_power(self) -> None:
        """Test the power function with two positive numbers.
        
        This function tests the power function from the calculator module.
        It checks if 2 to the power of 3 equals 8.
        
        Args:
        None
        
        Returns:
        None
        """
        self.assertEqual(power(2, 3), 8)

if __name__ == '__main__':
    unittest.main()