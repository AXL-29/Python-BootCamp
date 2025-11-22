# Reproduce the Bug:
# Some bugs are sneaky and only appear under certain conditions.
# To debug them, we first need to reliably reproduce the bug
# and then diagnose the problem to figure out which conditions trigger it.

from random import randint

dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

# The code block above can produce a bug.
# We need to reproduce it consistently to figure out how to fix it
# and understand what is causing it.

# print(dice_images[6])
# In this line, list indexing starts at 0, so the last valid index is 5.
# Since randint(1, 6) can return 6, if 6 is selected,
# it would cause an IndexError: list index out of range.

# To fix the code, change randint(1, 6) to randint(0, 5) or
# use randint(1, 6) and access dice_images[dice_num - 1] instead.
