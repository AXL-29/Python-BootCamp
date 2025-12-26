# Dynamic Type Casting - means converting a value from one data type to another while the program is running.

# Why it's needed?
    # User input, file data, and network data are often strings.
    # To do math or logic, you must cast them to the correct data type.

# Example 1: String -> Integer:
age = "21"
age = int(age)

print(age + 1)
# Without casting: "21" + 1 = TypeError.

# Example 2: Integer -> String:
score = 100
message = "Score: " + str(score)

print(message)
# Number must be converted to strings before concatenation.

# Example 3: Float -> Integer:
price = 19.99
rounded_price = int(price)

print(price)

# Example 4: Integer -> Float
count = 5
average = float(count)

print(average)

# Example 5: User input (real-world case):
user_input = input("Enter a number: ")
number = int(user_input)

print(number * 2)

# input() always return a string, so casting is required.