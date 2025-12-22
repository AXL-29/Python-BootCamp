import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# Loop through rows of a data frame
for (i, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)