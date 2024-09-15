num1=int(input("Enter Num1:"))
num2=int(input("Enter Num2:"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} is equal to {num2}")