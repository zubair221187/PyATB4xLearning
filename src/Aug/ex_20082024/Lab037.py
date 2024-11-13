# Conditions and Loops

# Write a program to take user age and let hi know if he can vote
#18

# Logic Building
# 1. user input - data type -> int
# o/p -> String -> user if he can go or not.

# 2. Rough Logic
# age > 18 -> print can vote
# age < 18 -> print can't vote

# 3. write the logic

age = input("Enter your age:\n")
age = int(age)

if age >= 18:
    print(f"Can Vote as your age is greater than {age}")
else:
    print(f"Can't Vote as your age is less than 18")