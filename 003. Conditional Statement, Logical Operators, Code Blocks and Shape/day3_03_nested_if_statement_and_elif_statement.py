# Nested if - means an if statement inside another if statement.
# It's used when you need to check more than one condition, step by step
# Syntax for nested if:
# if condition
#   if another condition:
#       do this
#   else:
#       do this
# else:
#   do this

# elif - means "else if"
# It's used when you want to check another condition if the first if condition is false.
# Syntax for elif:
# if condition1:
#   do A
# elif condition2:
#   do B
# else:
#   do this

print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("How old are you?: "))
    if age < 12:
        print("Ticket cost: $5")
    elif age <= 18:
        print("Ticket cost: $7")
    else:
        print("Ticket cost: $12")

else:
    print("Sorry, you can't ride the rollercoaster.")