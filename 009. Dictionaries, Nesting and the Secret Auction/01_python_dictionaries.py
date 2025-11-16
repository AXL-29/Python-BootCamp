# dictionary - is a built-in data type that lets you store data in key-value pairs.
# Think of it like a real dictionary:
# a word -> is the key
# the definition -> is the value.
# python syntax:
person = {
  "name": "Jade",
  "age": 20,
  "is_student": True
}

# "name", "age", "is_student" are keys
# "Jade", 20, True are values

print(person)

# adding key to a dictionary
person["height"] = 172
print(person)

# edit an item in a dictionary
person["name"] = "Jade Mark Gimpao"
print(person)

# Loop through a dictionary.
for key in person:
    print(key)          # print key in dictionary
    print(person[key])  # print value of the key

# wipe an existing dictionary
person = {}
print(person)