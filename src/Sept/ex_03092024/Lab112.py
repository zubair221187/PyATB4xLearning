class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

object_ref = Calc(10,5)
output = object_ref.sum()
print(output)