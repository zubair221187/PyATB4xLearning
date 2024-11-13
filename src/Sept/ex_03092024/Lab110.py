# Take input and create a class in Python

class Person:
    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = input("Enter your age\n")
        self.phone = input("Enter your phone\n")
        self.occupation = input("Enter your occupation\n")

    def display_information(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone is {self.phone}")
        print(f"Occupation is {self.occupation}")

# Create an Object
person1=Person()

# Call the display function

person1.display_information()
