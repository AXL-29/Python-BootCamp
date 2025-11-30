# Task 1 – Nested Loop over a List of Lists
# Goal: Practice for loop inside for loop.
# You have a “gradebook” where each inner list is a list of scores for a student.
# Example data (you can hard code this in your code):
    # [ [85, 90, 78], [92, 88, 95], [70, 75, 80] ]
# Your task:
    # Loop through each student.
    # For each student, loop through their scores.
    # Print something like:
        # Student 1 scores: 85 90 78
        # Student 2 scores: 92 88 95
        # Student 3 scores: 70 75 80
# After each student, also print their average score.
# -------------------------------------------------------------------------------------------------------------------- #

# Hard-coded gradebook: list of lists
gradebook = [
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80]
]

# We want "Student 1", "Student 2", etc.
# So we use range(len(gradebook)) or enumerate.

for i, scores in enumerate(gradebook, start=1):
    # i = student number (1, 2, 3, ...)
    # scores = the inner list, like [85, 90, 78]

    print(f"Student {i} scores:", end=" ")

    total = 0  # to compute average

    # Inner loop: go through each score for this student
    for score in scores:
        print(score, end=" ")
        total += score

    # After printing all scores, move to next line
    print()

    # Compute average
    average = total / len(scores)
    print(f"Student {i} average: {average:.2f}")
    print("-" * 30)  # just a separator
