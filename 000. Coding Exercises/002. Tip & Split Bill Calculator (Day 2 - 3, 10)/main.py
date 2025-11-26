# Tip & Split Bill Calculator (Days 2–3, 10)
# Concepts: numbers, arithmetic, rounding, if/elif/else, simple function with return value.

# Task: Build a restaurant bill helper that:
# Asks for:
    # Total bill amount
    # Percentage tip (e.g., 10, 12, 15)
    # Number of people splitting the bill

# Calculates:
    # The total amount including tip
    # How much each person should pay
    # Rounds the per-person amount to 2 decimal places.

# Rules:
# If the number of people is less than 1, show an error message and don’t do the calculation.
# Use a function (e.g., something that takes bill, tip, and people and returns per-person amount).

def calculate_bill_with_tip(bill, tip):
    """Takes the bill and tip, then returns the bill including tip."""
    tip = (tip / 100) * bill
    bill_with_tip = bill + tip
    return bill_with_tip

def calculate_bill_per_person(bill, tip, to_split):
    """Takes the bill, tip and to_split then returns the total_bill_per_person."""
    total_bill_per_person = calculate_bill_with_tip(bill, tip) / to_split
    return total_bill_per_person

is_valid = False
while not is_valid:
    try:
        # TODO 1: Ask for total bill amount:
        bill = float(input("What's the total bill? $: "))
        # TODO 2: Percentage tip
        tip = float(input("How much would you like to tip eg. 10, 12, 15: "))
        # TODO 3: Number of people splitting the bill
        is_valid_split = False
        while not is_valid_split:
            to_split = int(input("How many people will split the bill?: "))
            # TODO 4: If the number of people is less than 1, show an error message and don’t do the calculation.
            if to_split <= 1:
                print("At least 2 people are required to split the bill. Please try again!")
            else:
                is_valid_split = True    
        is_valid = True
    except ValueError:
        print("Please input a valid number!")

total_bill_per_person = calculate_bill_per_person(bill=bill, tip=tip, to_split=to_split)

print(f"The total bill per person is ${round(total_bill_per_person, 2)}.")
