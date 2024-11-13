def print_arguments(*args):
    # *arg = multiple argument with no limit, -> list
    # print(args[0])
    for i in args:
        print(i)


print_arguments("Zubair", "Abdulla", "Khadija")
print_arguments("Abdulla", "Khadija")
print_arguments("Khadija")
# print_arguments() - minimum 1 argument is required

print("Zubair")
print("Zubair", "Abdullah")
print("Zubair", "Abdullah", True)
print("Zubair", "Abdullah", True, False)