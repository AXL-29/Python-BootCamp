# 1. The first step of solving a problem is being able to describe the problem.

def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")

my_function()

# Describe the Problem - Write your answer as comments:
# 1. What is the for loop doing?
#   - Looping a block of code in range 1 - 20, exclusive of 20.
# 2. When is the function meant to print "You got it"
#   - When the i reaches number 20
# 3. What are your assumptions about the value of i?
#   - It will never get a value of 20, since in range(start, end) end number is exclusive therefore, 20 will never be reach.

# This code will fix that:
def my_function1():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function1()