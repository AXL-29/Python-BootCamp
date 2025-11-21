# Modifying Global Scope: You can force the code allow you to modify something with global if you use the
# global keyword before you use it.

# Example:
a = 1

# This will give you an error:
# def my_function():
#     a += 1
#     print(a)

# But this will work:
b = 1
def my_function2():
    global b    # used inside a function to say I want to use/modify the variable from the module level,
                # not create a new local one.

    b += 1
    print(b)

my_function2()