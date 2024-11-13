#
class Person:
    b = 11 # Instance - Belong to class
    c = 11  # Instance - Belong to class

    def print_info(self):
        global a
        a = "Hello"
        print(self.b)
        print(self.c)

object_Ref = Person()
object_Ref.print_info()
print(a)
# print(b) - cannot be used as i
# t is local variable