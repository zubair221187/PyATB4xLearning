class Dog:  # Class will always start with Capital letter
    # Attribute
    name = None
    breed = None
    colour = None

    # Behaviour
    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("Bark")

    def eat(self, food):
        print(food)


dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()
dog1.eat("Biscuit")

print("------------------------------")

dog2 = Dog()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)
dog2.sleep()

dog3 = dog1
