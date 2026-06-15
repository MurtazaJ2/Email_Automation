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
    # This test will pass for the next 60 seconds, and then fail forever after.
    # Current time recorded: time.time()
    # It simulates a flaky service dependency that goes down.
    current_time = time.time()
    import os
    with open("start_time.txt", "a+") as f:
        f.seek(0)
        start_time_str = f.read().strip()
        if not start_time_str:
            start_time_str = str(current_time)
            f.write(start_time_str)
        start_time = float(start_time_str)
    
    assert current_time - start_time < 60, "Service unavailable (timeout)"