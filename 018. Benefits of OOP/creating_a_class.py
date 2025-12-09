# A class is like a blueprint for creating objects.
# It defines the data (attributes) and behaviors (methods) that each object will have.

# Class = blueprint / template
# Object (instance) = an actual item created from that blueprint

# Why use classes?
# - Group related data and functions together
# - Organize code better
# - Reuse code easily
# - Represent real-world things in programming (like a car, student, bank account, etc.)

# Class names usually use PascalCase (ex: UserCountSize)
class User:
    # The constructor method runs automatically when you create an object.
    # It is always named __init__(self)
    def __init__(self, first_name, last_name, age):
        """
        Parameters:
        - self: refers to the object being created
        - first_name: the first name of the user (passed when creating object)
        - last_name: the last name of the user (passed when creating object)
        - age: the age of the user (passed when creating object)
        """
        # self.first_name, self.last_name, self.age are attributes of the object
        # They store the values passed as parameters
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        # default attribute value:
        self.follower = 0
        self.following = 0

    # method - function that belongs to an object (created from a class)
    # self - refers to the current object using the method
    def follow(self, user):
        user.follower += 1
        self.following += 1


    pass  # pass means "do nothing" here, just a placeholder

# Creating objects (instances) from the User class
# The values in parentheses are passed to the constructor parameters
user_1 = User("John", "Doe", 25)
user_2 = User("Jane", "Smith", 30)

# Adding additional attributes to objects (optional)
# Each object can have its own unique value
user_1.id = "001"
user_2.id = "002"

# Accessing attributes of objects
user_1.follow(user_2)
print(user_1.follower)
print(user_2.follower)
print(user_1.following)
print(user_2.following)
