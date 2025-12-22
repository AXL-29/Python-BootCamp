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