# To install Python packages, go to PyPI.org and search for the package you need.
# You can install it using "pip install <package_name>" in your terminal,
# or install it directly through PyCharm's package manager.

# Example: pip install PrettyTable

from prettytable import PrettyTable

table = PrettyTable()       # Creating a new object.
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])     # Calling a method associated with the object.
table.add_column("Type", ["Electric", "Water", "Fire"])                     # Calling a method associated with the object.

# Changing an Object Attributes:
table.align = "l"

print(table)
