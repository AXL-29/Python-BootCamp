# open() - is used to open a file so Python can use it.
# syntax: open("file.txt", "w")

# "w" (write mode) - 'w' means write
# it tells Python:
    # Create the file if it doesn't exist
    # Erase everything inside if it already exists.
    # Prepare it for writing new text

# write() - is used to put text into the file.
# syntax: file.write("Hello")
    # it means - "put this text into the file."

# Recommended way:
# with open("data.txt", "w") as file:
    # file.write("Hello World")

# One important warning:
    # open("data.txt", "w")

    # deletes existing content
    # if you want to add instead of delete, use "a".

# to write
with open("data.txt", "w") as file:
    file.write("\nHello World!")

# to append
with open("data.txt", "a") as file:
    file.write("\nHello World!")

# to read
with open("data.txt", "r") as file:
    content = file.read()
    print(content)