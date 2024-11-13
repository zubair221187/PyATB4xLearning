# Write a python program to calculate the
# Area of a circle given its radius using the formula
# ''' area = 3.14 x r^2

# Logic Building Formula

# Step 1 Figure out the inputs and output
# input -> r -> data type -> float
# pi -> 3.14
# power -> pow or ** -> any

# o/p -> float - area , print area

# Step 2
# rough logic = area = 3.14 * pow(r,2)

# Step 3 - Write the logic
import math

radius = float(input("Enter the radius of the circle\n"))
print(radius)
area = math.pi * math.pow(radius,2)
area2 = 3.14 * radius**2
print("Area of the circle is -->", area)
print("Area of the circle is -->", area2)
print(f"Area of the circle is --> {area:.2f}")
print(3.14*float(input("Enter the radius\n"))**2) # one liner