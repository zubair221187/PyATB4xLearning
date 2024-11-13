class Car:

    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name" + self.name)
        print("Starting a car with the name" + self.make)
        print("Starting a car with the name" + self.model)

lambo = Car("lambo","V2","2024")
lambo.start_engine()

xuv = Car("XUV","V6","2023")
lambo.start_engine()