# Study Session Planner (Days 5–7, 9)
# Concepts: lists, loop, functions, basic nesting.
# Task: Make a study session planner:
# Ask the user for:
    # How many subjects to study today
    # For each subject: name + time in minutes
# Store the subjects and times in a suitable structure.

# Print:
# Numbered list of subjects with time per subject
# Total study time
# Optionally, include breaks (e.g., 5 minutes per subject) and calculate total time including breaks.

# Rules:
# Use at least one function to handle adding subjects or printing the summary.
# Loop correctly over the stored data.

subject_with_time = ([],[])

num_of_subject = int(input("How many subjects do you want to study today?: "))

for _ in range(num_of_subject):
    subject = input("Enter subject name: ")
    time = int(input(f"Enter time in minutes for {subject}"))
    subject_with_time[0].append(subject)
    subject_with_time[1].append(time)

print(subject_with_time)