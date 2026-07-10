def divide(a: float, b: float) -> float:
    """
    Divide two numbers.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient.

    Raises:
        ZeroDivisionError: If the divisor is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return a / b


def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract two numbers.

    Args:
        a (float): The minuend.
        b (float): The subtrahend.

    Returns:
        float: The difference.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product.
    """
    return a * b


def power(a: float, b: float) -> float:
    """
    Raise a number to a power.

    Args:
        a (float): The base.
        b (float): The exponent.

    Returns:
        float: The result.
    """
    return a ** b