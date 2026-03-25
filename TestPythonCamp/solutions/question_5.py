"""Reference solution for question 5."""


def find_top_student(scores):
    if not scores:
        raise ValueError("scores cannot be empty")
    return max(scores, key=scores.get)
