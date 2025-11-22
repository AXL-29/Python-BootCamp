# 3. Play as a Computer:
# Playing computer is an important debugging skill.
# You need to step through your code line by line as if you were
# the computer to figure out what is going wrong.

year = int(input("What's your year of birth: "))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z")

# This block of code will skip all the conditions for some years.
# For example, if you enter 1994, it doesn't satisfy either condition
# (not > 1994 and not < 1994), so nothing gets printed.
# To fix this, we need to set either "==" or ">=" 1994.