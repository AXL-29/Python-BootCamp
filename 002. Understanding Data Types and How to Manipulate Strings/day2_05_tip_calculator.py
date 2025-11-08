print("Welcome to the tip calculator")

bill = float(input("What was the bill: $"))
tip = float(input("How much tip would you like to give: "))
num_of_people = int(input("How many people would split the bill: "))

tip = bill * (tip / 100)
total_bill = bill + tip
pay_per_person = total_bill / num_of_people

print(f"Each person should pay: ${round(pay_per_person, 2)}")

