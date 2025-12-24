# Unlimited Arguments: a function can accept any number of arguments, 
# without knowing how many in advance.

# What does *args mean?
# *args allows a function to receive unlimited positional arguments.
# all the arguments are collected into a tuple.



def add (*args): 
    result = sum(args)
    return result

sum_of_numbers = add(1, 2, 3, 4, 5, 6, 7, 8)
print(sum_of_numbers)