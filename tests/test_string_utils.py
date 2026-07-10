import unittest
from app.string_utils import lowercase

def test_lowercase() -> None:
    """
    Test the lowercase function from app.string_utils.
    """

    class TestLowercaseFunction(unittest.TestCase):
        def test_lowercase_function(self) -> None:
            """
            Test the lowercase function with a specific input.
            """
            self.assertEqual(lowercase("HELLO"), "hello")

    if __name__ == "__main__":
        unittest.main(exit=False)