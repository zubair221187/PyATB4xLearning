squares = [1, 4, 9, 16, 25]

# List is mutable in nature
# mutable - change -

squares[3] = 64
print(squares)

# Tuple - Collection of Items

my_tuple = (1, 4, 9, 16, 25)
# my_tuple[3] = 64 # Immutable in nature
print(my_tuple)  # tuple object does not support item assignment

shopping_list_wife = ["bread", "butter", "paneer"]
shopping_list_wife[2] = "milk"
print(shopping_list_wife)

# Real world project
# Thetestingacademy.com, sdet.live

my_tuple = ("tta.com", "sdet.livve")
print(my_tuple)

my_list = list(my_tuple)
print(my_list)

my_list = tuple(my_list)
print(my_list)

my_tuple1 = (1, 2, 3, 3)  # Tuple can handle duplicate values
print(my_tuple1)

# Real case, where we Tuples

API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])
print(API_URLSs[1])