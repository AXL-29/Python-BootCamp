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

def add_break_time():
    """Let the user decide if they want to add a break in minute per subject and return the total minute."""
    while True:
        add_break = input("Do you want to add break? (yes/no): ").lower()
        if add_break == "yes":
            break_time = int(input("How long is each break (in minutes): "))
            break_time *= len(subject_with_time[1])
            return sum(subject_with_time[1], break_time)
        elif add_break == "no":
            return sum(subject_with_time[1])

        else:
            print("Invalid input, please type 'yes' or 'no' only!")

def add_subject_time():
    while True:
        try:
            num_of_subject = int(input("How many subjects do you want to study today?: "))
            break
        except ValueError as err:
            print(f"Error: {err}, please try again!")

    for _ in range(num_of_subject):
        subject = input("Enter subject name: ")
        time = int(input(f"Enter time in minutes for {subject}: "))
        subject_with_time[0].append(subject)
        subject_with_time[1].append(time)


def study_plan():