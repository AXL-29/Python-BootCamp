student_scores = [88, 92, 76, 81, 95, 67, 73, 89, 90, 78,
                  84, 91, 69, 100, 85, 77, 93, 80, 72, 68,
                  96, 87, 94, 79, 83]

# calculate the total score using the for loop.

total_score = 0

for score in student_scores:
    total_score += score

print(total_score)

# code challenge: get the highest score (max) using for loop

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)