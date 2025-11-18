# syntax: function with inputs
# def my_function(something):
#   do this with something
#   then do this
#   Finally do this

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# syntax: functions with outputs
def format_name(f_name, l_name):
    # title() is use to capitalize the first letter of each word
    formated_first_name = f_name.title()
    formated_last_name = l_name.title()

    # return is how you send an answer back to where the function was called.
    formatted_full_name = formated_first_name + " " + formated_last_name
    return formatted_full_name

print(format_name(first_name, last_name))