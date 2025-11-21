# Python is a bit different from other programming languages in that it does NOT have block scope.
# This means that variables created nested in other blocks of code e.g. for loops, if statements,
# while loops, etc. don't get local scope. They are given function scope if they are within a function
# or global scope if they are not.

# In python, if / for / while / try / with blocks do not create a new scope.
# Example: Block doesn't create scope.

if True:
    x = 10  # defined inside the if-block.

print(x)    # variable x still works and print 10.

# In languages with block scope, x would "die" after the if block.
# In Python, it escapes to the surrounding scope (here: the module/global scope).

# same with for:
for i in range(3):
    y = i

print(i)
print(y)