# Unlimited Keywords Arguments - it lets a function accept any number of named arguments.
# In Python, all those named arguments are collected into a dictionary.

# Basic Example:
def show_info(**kwargs):
    print(kwargs)

show_info(name="Jade", role="NOC Analyst", shift="Night")

# get() is a dictionaty method used to safely retrieve a value by it's key

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(model="GT-R")
print(my_car.model)