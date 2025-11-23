# FizzBuzz Debugging

# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 or number % 5 == 0:
#             print("FizzBuzz")
#         if number % 3 == 0:
#             print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         else:
#             print([number])

# The code is intended to print the solution to the FizzBuzz game:
# - It should print each number from 1 to x, where x is the input number.
# - If a number is divisible by 3, it should print "Fizz" instead of the number.
# - If a number is divisible by 5, it should print "Buzz" instead of the number.
# - If a number is divisible by both 3 and 5 (e.g., 15), it should print "FizzBuzz".

# Answer:
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# The original code uses multiple independent if statements, which causes the value to go through multiple checks.
# The "or" operator returns True if either condition 1 or condition 2 is True, or both are True; it only returns False when both are False.
# To fix the logic, using elif ensures that if the first condition is false, the next condition is checked, avoiding overlapping outputs.
# Also, in the else statement, the number should be printed directly, not inside square brackets, to match the expected output.