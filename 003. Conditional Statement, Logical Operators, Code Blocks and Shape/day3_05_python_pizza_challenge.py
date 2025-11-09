# Write a Pizza Deliver Program
# Prices:
# Small Pizza(S): $15
# Medium Pizza(M): $20
# Large Pizza(L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N) +$3
# Add extra cheese for any pizza size (Y or N) +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? (S, M, or L): ")
pepperoni = input("Do you want pepperoni on your pizza? (Y or N): ")
extra_cheese = input("Do you want an extra cheese? (Y or N): ")

bill = 0

if size.upper() == "S":
    bill += 15
    if pepperoni.upper() == "Y":
        bill += 2
elif size.upper() == "M":
    bill += 20
    if pepperoni.upper() == "Y":
        bill += 3
elif size.upper() == "L":
    bill += 25
    if pepperoni.upper() == "Y":
        bill += 3
else:
    print("Please input a valid size! Thank you!")

if extra_cheese.upper() == "Y":
    bill += 1

print(f"You're total bill would be ${bill}")