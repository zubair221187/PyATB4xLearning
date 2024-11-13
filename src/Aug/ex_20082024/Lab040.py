# Problem find the Max between 3 numbers

# Logic ? If else -> 1 condition
# more than 1 condition -> if elif else

num1 =int(input("Enter num1: "))
num2 =int(input("Enter num2: "))
num3 =int(input("Enter num3: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the greater than {num2} & {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the greater than {num1} & {num3}")
else:
    print(f"{num3} is the greater than {num1} & {num2}")