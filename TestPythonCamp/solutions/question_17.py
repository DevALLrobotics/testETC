"""Reference solution for question 17."""


def get_last_element(items):
    if not items:
        raise ValueError("items cannot be empty")
    return items[-1]
