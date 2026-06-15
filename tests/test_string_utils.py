def test_lowercase():
    from app.string_utils import lowercase
    assert lowercase("HELLO") == "hello"
