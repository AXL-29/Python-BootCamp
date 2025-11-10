# IndexError: list index out of range - this error happens when you try to access list position(index) that doesn't exist.
# Python lists starts at index 0, so the last valid index is len(list) - 1.

fruits = ["banana", "mango", "apple", "guava", "jackfruit"]

# to avoid errors accesing the last index use the 'len(list)-1'.

print(len(fruits)-1)

index_of_fruits = len(fruits)
print(fruits[index_of_fruits - 1])

# nested list - means a list inside another list.

fruits = [
    "apple", "banana", "mango", "orange", "grape", "pineapple", "watermelon",
    "strawberry", "cherry", "kiwi", "papaya", "pear", "peach", "blueberry", "avocado"
]

vegetables = [
    "carrot", "broccoli", "spinach", "tomato", "potato", "onion", "garlic",
    "cabbage", "lettuce", "eggplant", "cucumber", "bell pepper", "cauliflower", "okra", "corn"
]

# combine them (nested list)
foods = [fruits, vegetables]

print(foods)
