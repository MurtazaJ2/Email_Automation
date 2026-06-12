from app.calculator import divide

def test_divide():
    assert divide(10, 2) == 5

def test_add():
    from app.calculator import add
    assert add(2, 3) == 5