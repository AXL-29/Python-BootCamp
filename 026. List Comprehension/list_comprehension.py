# list comprehension - is a short and clean way to create a list from another list (like a list, range, or string) in a single line.

# basic syntax: new_list = [expression for item in iterable]

numbers = [1, 2, 3, 4, 5, 6]
squares = [n * n for n in numbers]
print(squares)

name = "Jade Mark Gimpao"
letter_list = [letter for letter in name]
print(letter_list)

doubled = [d * 2 for d in range(1, 5)]
print(doubled)

# conditional list comprehension - lets you add conditions to decide which items are included
# and/or how they're transformed.

# conditioanl filtering - keeps items only if the condition is true. 
# syntax: [expression for item in iterable if condition]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# conditional expression (if-else) - this changes the value added to the list, not whether it's included.
# syntax: [true_value if condition else false_value for item in iterable]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)