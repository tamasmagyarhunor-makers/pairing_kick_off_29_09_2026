def make_initials(name):
    if isinstance(name, str):
        names = name.upper().split()
        first_initial = names[0][0]
        last_initial = names[1][0]

        return first_initial + "." + last_initial
    raise Exception("Only strings can be attempted for name initials!")