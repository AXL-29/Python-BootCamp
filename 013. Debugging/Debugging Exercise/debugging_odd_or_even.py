# Debugging Odd or Even

# def odd_or_even(number):
#     if number % 2 = 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."


# Answer:

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

# The bug was in the if condition:
# It used "=" (assignment) instead of "==" (comparison) to check if number % 2 is equal to 0.