# User Defined
# 1. They can't return --> non return
# 2. They can return something
# They have parameters
# They don't have parameters / arguments

# 1. They can't return -> non return
# No Return Type and No Parameter / Argument

def greet():
    print("Hello World")


result = greet()
print(result)


# 2. # No Return Type and with Argument

def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Zubair")


# 3. # No Return Type and with Default Argument

def say_hello_default_arg(name="Zubair"):
    print("Hello,", name)


say_hello_default_arg()
say_hello_default_arg("Abdullah")
say_hello_default_arg(name="Bareerah")  # positional argument


def multiple_args(name1="Zubair", name2="Bareerah", name3="Abdullah"):
    print("Multiple Arguments : ", name1, name2, name3)


multiple_args(name1="Khadija", name2="Khansa", name3="Aqsa")
multiple_args()


# 4. Argument + Return Type

def sum_of_two_number(num1, num2):
    return num1 + num2


result = sum_of_two_number(10, 34)
# result= sum_of_two_number(1) # will throw error, as no default value
print(result)