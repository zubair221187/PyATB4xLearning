# List
# List - Collections of Items ( Duplicate is allowed )

my_list = [1, 2, 3]  # same type of data
my_list2 = [1, True, "Zubair", 12.34]

print(my_list)
print(len(my_list))
print(my_list2)
print(len(my_list2))

print(my_list[0])
print(my_list[1])
# print(my_list[10])  # list index out of range - exception

# Indexing
my_list[0] = "Zubair"
my_list[1] = "Iliyas"
my_list[2] = "Hangargekar"

print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

for element in my_list:
    print(element)

for i in range(1, 10):
    print(i)

# range (1,10,1) -> list -> [1,2,3,4,5,6,7,8,9]

# Append

my_list.append(4)  # Append object to the end of the list
my_list.extend([5, 6, 7, 8])  # to add multiple elements
print(my_list)

# Insert

my_list.insert(1, "Abdullah")
print(my_list)

my_list[1] = "Khadija"
print(my_list)

my_list.insert(-1, "Khansa")  # negative index adds in reverse order
print(my_list)

# remove()

my_list.remove("Khansa")
print(my_list)

copy_of_my_list = my_list.copy()

print(my_list)
print(copy_of_my_list)

my_list[0] = 1
my_list[1] = 2
my_list[2] = 3
my_list[3] = 4

print(my_list)

my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

my_list.sort(reverse=False)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)