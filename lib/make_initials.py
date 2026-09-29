def make_initials(name):
    names = name.upper().split()
    first_initial = names[0][0]
    last_initial = names[1][0]

    return first_initial + "." + last_initial