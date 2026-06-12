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