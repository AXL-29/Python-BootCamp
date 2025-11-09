# Logical Operatos - are used to combine multiple condition in an if statement.
# They help Python decide if more than one condition is true.

# Three Main Logical Operators
# and - True if both conditions are True.
# or  - True if at least one condition is True.
# not - Reverse the result - True becomes False, False becomes True.

print("Welcome to the rollercoaster!")
bill = 0
height = float(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("How old are you?: "))
    if age < 12:
        print("Child ticket cost: $5")
        bill = 5
    elif age <= 18:
        print("Youth ticket cost: $7")
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
        print("You're free to ride. Enjoy!")
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