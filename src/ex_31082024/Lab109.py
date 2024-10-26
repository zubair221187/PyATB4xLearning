# Constructor
# Special function in Class, __init__()
# It will be automatically called when object is created

class Dog:
    name = None

    def __init__(self, name, age):
        print("I will be called automatically when you create an Object")
        self.name = name
        self.age = age

    def sleep(self):
        print("Sleeping")
        print("Who is sleeping --> ", self.name, self.age)


dog1 = Dog("Chow", 10)
print(dog1.name)
print(dog1.age)
dog1.sleep()

dog2 = Dog("Mow", 20)
print(dog2.name)
print(dog2.age)
dog2.sleep()