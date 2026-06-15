from app.calculator import divide

def test_divide():
    assert divide(10, 2) == 5

def test_add():
    from app.calculator import add
    assert add(2, 3) == 5

def test_subtract():
    from app.calculator import subtract
    assert subtract(5, 2) == 3

def test_multiply():
    from app.calculator import multiply
    assert multiply(3, 4) == 12

def test_power():
    from app.calculator import power
    assert power(2, 3) == 8

def test_flaky_service():
    import time
    # This simulates a flaky external API that goes down at a specific UNIX timestamp.
    # It will pass initially, then fail forever after the timestamp.
    assert time.time() < 1781500509, "503 Service Unavailable: The mock flaky service went down!"