# A debugger - is a tool (usually built into your code editor or IDE)
# that helps you find and fix bugs in your program letting you pause and inspect it while it's running.

# What a debugger can do?:
# 1. Set breakpoints
#   - You can pick a line of code where the program should pause.
#   - When the program reaches that line, it stops so you can look around.

# 2. Step through code
#   - Run your program one line at a time:
#   - Step over – run the current line, go to the next.
#   - Step into – go inside a function call.
#   - Step out – finish the current function and go back.

# 3. Inspect variables
#   - While paused, you can see the value of variables:
#       x = ?
#       user_input = ?
#       result = ?
#   - This helps you understand why your program is behaving wrong.
#
# 4. Watch expressions
#   - You can set “watches” on values like total_price, len(list), etc.
#   - The debugger will auto-update these as your code runs.

# 5. Check the call stack
#   - Shows which functions called which, in what order.
#   - Helpful when you have deep function calls and an error happens somewhere inside.

import random

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item += item
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])