# Errors vs Exceptions:

# Errors:
    # Usually syntax or logical mistakes
    # Stop the program immediately

# Exceptions:
    # Happen during runtime
    # Can be handled so the program doesn't crash

# Handling Exceptions with try / except
# Basic Structure:
# try:
    # code that might fail
# except:
    # runs if an error occurs
# else:
    # runs if no error occurs
# finally:
    # always runs

try: 
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as err:
    print(f"The key {err} has does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")