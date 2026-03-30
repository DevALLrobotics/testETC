"""Reference solution for question 20."""


def get_initials(full_name):
    words = full_name.split()
    return "".join(word[0].upper() for word in words)
