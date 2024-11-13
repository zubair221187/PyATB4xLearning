class Person:
    # Class Variable
    # Instance Variabls
    # name = "Zubair"

    def __init__(self, name):
        self.name = name

    def walk(self, name):
        self.name = name
        print(self.name)


zubair = Person("Abdullah")
Khadija = Person("Khadija")
print(zubair.name)
print(Khadija.name)
