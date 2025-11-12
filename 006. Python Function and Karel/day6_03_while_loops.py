# while loop - is used repeat code of block as long as a certain condition is True.
# The loop just keeps running until the condition becomes False.

# Syntax:
# while condition_is_true:
#   code to run repeatedly.

# condition - a statement that is checked before each loop.
# if it's True, the code inside the loops runs.
# if it's False, the loop stops.

number = 10

while number > 0:
    number -= 1
    print(number)

# The main danger of a while loop is that it can easily lead to an 
# infinite loop — meaning the code keeps running forever and never stops.