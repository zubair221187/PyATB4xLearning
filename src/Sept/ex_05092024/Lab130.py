class GrandParent:
    gold ="1 KG Gold"

    def grand_parent_method(self):
        print("Grand Parent Method")


class Parent(GrandParent):
    diamond = "22 karat"

    def parent_method(self):
        print("Parent Method")


class Child(Parent):
    btc= "1 BTC"

    def child(self):
        print("Child Method")

c=Parent()
c.grand_parent_method()
print(c.diamond)