from lib.make_initials import make_initials
import pytest

def test_make_initials_will_smith_returns_ws():
    result = make_initials("Will Smith")

    assert result == "W.S"

def test_make_initials_returns_initials_correctly_even_with_lowercase_name():
    assert make_initials("sophie lauren") == "S.L"

def test_exception_when_not_string():
    with pytest.raises(Exception) as error:
        make_initials(1)
    
    error_message = str(error.value)

    assert error_message == "Only strings can be attempted for name initials!"
