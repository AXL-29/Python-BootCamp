# JSON(JavaScript Object Notation) is a lightweight data format
# used to store and exchange data between programs

# In Python, JSON is commonly used to:
    # Save data to files
    # Load saved data back into programs
    # Work with APIs and configuration files

import json

# Writing data to JSON(json.dump)

data = {
    "name": "Jade",
    "language": "Python",
    "level": "Beginner"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# This saves the dictionary into a file called data.json

# Reading data from JSON(json.load)
with open("data.json", "r") as file:
    data = json.load(file)

print(data["name"])

# Update data from JSON
data.update(data)

# Saving the data
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
