class Person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour
    def talk(self):  # self - this , self will be the first argument in every behaviour
        print("I can talk")

    def sleep(self, name):  # Arg with no return
        print("I am a Method !!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with return
        print("I am a Method !!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):  # No Arg with return
        return "I am walking"

    # Create an object of the Class
    # ObjectRef = ClassName () --> Object


zubair = Person()
zubair.name = "zubair"
print(zubair.name)

Abdullah = Person()
zubair.name = "Abdullah"
print(zubair.name)