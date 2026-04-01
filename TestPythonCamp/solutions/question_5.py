"""Reference solution for question 5."""


# def find_top_student(scores):
#     if not scores:
#         raise ValueError("scores cannot be empty")
#     return max(scores, key=scores.get)

def find_top_student(scores):
    if not scores:
        raise ValueError("scores cannot be empty")
    
    top_student = None
    top_score = None
    
    for student in scores:
        if top_score is None or scores[student] > top_score:
            top_student = student
            top_score = scores[student]
    
    return top_student