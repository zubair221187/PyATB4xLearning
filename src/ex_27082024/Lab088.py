# def sum_three_num(a,b,c):

# return a+b+c

sum = lambda a, b, c: a + b + c

print(sum(3, 4, 5))


def find_odd_even(num):
    if num % 2 == 0:

        print("Even")

    else:

        print("Odd")


find_odd_even(5)

op = lambda num: "Even" if num % 2 == 0 else "Odd"

print(op(6))
