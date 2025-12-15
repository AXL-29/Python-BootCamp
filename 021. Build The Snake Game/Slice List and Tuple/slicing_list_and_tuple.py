# Slicing is a way to extract a portion of a list, tuple, or string without modifying the original object.
# You use the [start: stop: step] syntax.

# | Part    | Meaning                                                |
# | ------- | ------------------------------------------------------ |
# | `start` | Index to start (inclusive)                             |
# | `stop`  | Index to end (exclusive)                               |
# | `step`  | How many items to skip each time (optional, default=1) |

# Example with list
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])      # [20, 30, 40] → from index 1 to 3
print(numbers[:3])       # [10, 20, 30] → start is 0
print(numbers[3:])       # [40, 50, 60] → till the end
print(numbers[::2])      # [10, 30, 50] → every 2nd element
print(numbers[::-1])     # [60, 50, 40, 30, 20, 10] → reverse


# Example with tuple
colors = ("red", "green", "blue", "yellow")

print(colors[1:3])       # ('green', 'blue')
print(colors[:2])        # ('red', 'green')
print(colors[::2])       # ('red', 'blue')

