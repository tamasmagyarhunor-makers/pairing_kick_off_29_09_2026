## 1 the problem
```
As a User
So that I can have names shortened
I want to be able to get initials of a fullname
```

## 2 the function(class) signature
```python
# Parameters:
# - fullname, str, eg. "Will Smith"
# Return: 
# - string, eg. W.S
# Side effects:
# - None
def make_initials(fullname):
    pass
```

## 3 examples
```python
# input - output 
make_initials("Will Smith") => "W.S"

make_initials("sophie lauren") => "S.L"

make_initials(1) => raise Exception("Only strings can be attempted for name initials!")

make_initials(True) => raise Exception("Only strings can be attempted for name initials!")
```