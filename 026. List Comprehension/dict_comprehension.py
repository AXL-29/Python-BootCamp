# dictionary comprehension - a concise, one-line way to create a dictionary
#                            by generating key-value pairs from an iterable,
#                            optionally including a condition to filter or 
#                            transform the items.

# Key points:
    # Produces a dictionary ({key: value, ...})
    # Can include expressions for keys and/or values
    # Can includes conditions to filter which items are added.
    # Equivalent to creating a dictionary with a for loop, but in one line.

# Syntax: {key_expression: value_expression for item in iterable if condition}

import random


numbers = [1, 2, 3, 4, 5, 6, 7]
squares = {n: n**2 for n in numbers}
print(squares)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

passed_student = {student:score for student, score in student_scores.items() if score > 60}
print(passed_student)