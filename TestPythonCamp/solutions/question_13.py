"""Reference solution for question 13."""


def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
