# Study Session Planner (Days 5–7, 9)
# Concepts: lists, loop, functions, basic nesting.

# We’ll store:
# subjects_with_times[0] -> list of subject names
# subjects_with_times[1] -> list of times in minutes
subjects_with_times = ([], [])
break_time_per_subject = 0


def add_subjects_and_breaks():
    """
    Ask the user how many subjects they want to study today,
    then for each subject ask for its name and study time (in minutes).

    Also asks if the user wants to include breaks, and if yes,
    how long each break is (in minutes).

    Populates:
        subjects_with_times[0] -> subject names
        subjects_with_times[1] -> subject times in minutes
    Sets:
        break_time_per_subject (global) -> break duration per subject in minutes
    """
    global break_time_per_subject

    # Ask for number of subjects
    while True:
        try:
            num_subjects = int(input("How many subjects do you want to study today?: "))
            if num_subjects <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError as err:
            print(f"Error: {err}, please try again!")

    # Ask for each subject and its time
    for _ in range(num_subjects):
        subject_name = input("Enter subject name: ").strip()
        while not subject_name:
            print("Subject name cannot be empty.")
            subject_name = input("Enter subject name: ").strip()

        while True:
            try:
                subject_time = int(input(f"Enter time in minutes for {subject_name}: "))
                if subject_time <= 0:
                    print("Please enter a time greater than 0.")
                    continue
                break
            except ValueError as err:
                print(f"Error: {err}, please try again!")

        subjects_with_times[0].append(subject_name)
        subjects_with_times[1].append(subject_time)

    # Ask if user wants to include breaks
    while True:
        add_break = input("Do you want to include breaks? (yes/no): ").strip().lower()
        if add_break == "yes":
            while True:
                try:
                    break_time_per_subject = int(input("How long is each break (in minutes)?: "))
                    if break_time_per_subject < 0:
                        print("Break time cannot be negative.")
                        continue
                    break
                except ValueError as err:
                    print(f"Error: {err}, please try again!")
            break
        elif add_break == "no":
            break_time_per_subject = 0
            break
        else:
            print("Please type 'yes' or 'no' only!")


def calculate_total_study_time(subjects_and_times, break_minutes_per_subject):
    """
    Calculate total study time including optional breaks.

    Args:
        subjects_and_times: tuple (subject_names, subject_times)
        break_minutes_per_subject: int, break duration per subject in minutes

    Returns:
        int: total planned time in minutes (study + breaks)
    """
    subject_times = subjects_and_times[1]
    total_study_minutes = sum(subject_times)

    total_break_minutes = len(subject_times) * break_minutes_per_subject
    return total_study_minutes + total_break_minutes


def study_plan():
    """
    Main function to run the study session planner.
    """
    add_subjects_and_breaks()
    total_time = calculate_total_study_time(subjects_with_times, break_time_per_subject)

    print("\n📚 Study Plan for Today:")
    for index in range(len(subjects_with_times[0])):
        subject_name = subjects_with_times[0][index]
        subject_time = subjects_with_times[1][index]
        print(f"{index + 1}. {subject_name} – {subject_time} minutes")

    if break_time_per_subject > 0:
        print(f"\nBreak per subject: {break_time_per_subject} minutes")

    print(f"\nTotal study time (including breaks if any): {total_time} minutes")


study_plan()
