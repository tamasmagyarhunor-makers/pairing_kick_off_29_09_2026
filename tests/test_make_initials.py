from lib.make_initials import make_initials

def test_make_initials_will_smith_returns_ws():
    result = make_initials("Will Smith")

    assert result == "W.S"