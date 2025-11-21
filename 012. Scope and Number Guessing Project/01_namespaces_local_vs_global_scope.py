# scope - is simply where a variable can be seen and used in your code
#         think of it as the "visibility range" of a variable.

# The four main scopes (LEGB rule)
# 1. L - Local: Inside the current function.
# 2. E - Enclosing: In outer function (for nested functions)
# 3. G - Global: At the top level of the file (module)
# 4. B - Built-in: Names that python provides by default (like print, len, etc.).

# Local Scope Example:
def my_function():
    a = 10      # x is local to my_function
    print(a)

my_function()
# print(x)      # since x is a local to my_function is not defined here

# Global Scope Example:
x = 2

def my_function2():
    print(x)    # can see the global x (variable)

my_function2()
print(x)        # also works outside the function.
# x is defined outside any function, so it's global in this file.

# Enclosing(nested functions) + nonlocal Example:
def outer():
    b = 10

    def inner():
        nonlocal b  # use to modify the outer() local variable, only works in enclosing function scopes.
        b = 20      # modifies x from the outer()

    inner()
    print(b)        # 20
outer()
