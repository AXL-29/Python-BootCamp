def clear():
    print("\n" * 100)

again = True
bid_dictionary = {}

while again:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bid_dictionary[name] = bid

    invalid_input = True
    while invalid_input:
        other_bidders = input("Is there any other bidders? (y/n): ").lower()

        if other_bidders == "n":
            again = False
            invalid_input = False
        elif other_bidders == "y":
            clear()
            invalid_input = False
        else:
            print("Please enter 'y' or 'n' only.")

# Make sure bids are numbers
for name in bid_dictionary:
    bid_dictionary[name] = int(bid_dictionary[name])

# Find the highest bid
highest_bid = 0
winner = ""

for name, bid in bid_dictionary.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name

print(f"The winner is {winner} with a bid of ${highest_bid}.")
