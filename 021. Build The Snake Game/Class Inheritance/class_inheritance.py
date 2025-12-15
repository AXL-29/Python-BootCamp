# Class Inheritance is an Object-Oriented Programming (OOP) concept where a child class (subclass)
# inherits properties and behaviors (Variables and methods) from a parent class (super class)

# In simple terms: One class is built on top of another class.

# Why use inheritance?
# Inheritance helps you:
    # Reuse code
    # Avoid duplication
    # Organize related classes
    # Make programs easier to maintain and extend

# Basic idea:
    # Parent class - contains common features
    # Child class - inherits those features and can add or modify behavior

# Key Terms:
    # Parent / Base class - The class being inherited from
    # Child / Derived class - The class that inherits
    # Override - Child class replaces a parent method
    # super()   - Used to call parent class methods

# When to use inheritance
    # There is an "is-a" relationship
        # Dog is an Animal
        # Student is a Person

    # Don't use inheritance if the relationship is "has-a"
        # Car has an Engine - use composition instead. 

# syntax:
    # class ClassName(ParentClass):
        # def __init__(self):
            # super().__init__()

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()