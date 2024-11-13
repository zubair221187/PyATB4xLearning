# Functions Scope
global_b = 12


def my_function():
    a = 10  # local variable, within the function only
    print(a)
    print(global_b)


# print(a) -- will throw error

def f1():
    print(global_b)


my_function()
print(global_b)
f1()