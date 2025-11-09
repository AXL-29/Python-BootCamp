# Multiple if statement - is when you write more than one if statement separately, not connected by elif or else.
# Each "if" is independent, so Python checks all of them, no matter what.

print("Welcome to the rollercoaster!")
bill = 0
height = float(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("How old are you?: "))
    if age < 12:
        print("Child ticket cost: $5")
        bill += 5
    elif age <= 18:
        print("Youth ticket cost: $7")
        bill += 7
    else:
        print("Adult ticket cost: $12")
        bill += 12
    
    # want photos condition.
    want_photos = input("Do you like to avail photos? press 'y' for YES and 'n' for NO: " )
    if want_photos.lower() == "y":
        print("Additional $3")
        bill += 3
            
    print(f"You're total bill would be ${bill}")

else:
    print("Sorry, you can't ride the rollercoaster.")