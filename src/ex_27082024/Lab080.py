# Understanding Decorators in Python

def my_decorator(func):
    # in decorator we have two parts
    # wrapp & call
    def wrapper():
        print("1.Something is happening before the function is called")
        print("2.Add Helmet,Gloves , Knee Guards")
        func()
        print("3.Something is happening after the functions is called")
        print("4.Secure Driving")

    return wrapper()


# function definition
# @my_decorator
# def drive_bike():
#    print("I am driving")

@my_decorator
def drive_scooty():
    print("Normal Function")


drive_scooty()