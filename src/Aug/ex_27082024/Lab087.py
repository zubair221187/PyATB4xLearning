# lambda expression
# A lambda is an anonymous function that returns some form of data

def add_10(n):
    return n + 10


o = add_10(100)
print(o)

o = lambda n: n + 10  # argument + return value
print(o(100))


def mul(a, b):
    return 1 * b


oo = lambda a, b: a * b
print(oo(3, 4))