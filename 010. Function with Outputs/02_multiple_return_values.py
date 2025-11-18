# functions terminate at the return keyword. If you write code below the return statement that code will not be executed.

def format_name(f_name, l_name):
    formatted_first_name = f_name.title()
    formatted_last_name = l_name.title()

    # however you can use multiple return using conditional returns:
    if formatted_first_name == "":
        return f"result {formatted_last_name} "
    elif formatted_last_name == "":
        return f"result {formatted_first_name}"
    else:
        return formatted_first_name + " " + formatted_last_name

    print("This won't work")    # return is the end of function.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(format_name(first_name, last_name))