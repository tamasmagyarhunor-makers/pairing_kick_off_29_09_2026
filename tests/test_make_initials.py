from lib.make_initials import make_initials

def test_make_initials_will_smith_returns_ws():
    result = make_initials("Will Smith")

    assert result == "W.S"

def test_make_initials_returns_initials_correctly_even_with_lowercase_name():
    assert make_initials("sophie lauren") == "S.L"