# Dict
# Collection of unique items
# Key and Value
# name -> "Zubair"

student_info = {"name": "Zubair",
                "age": 65,
                "age": 67,
                "address": "Pune"}

print(student_info)
print(student_info["name"])
print(student_info["age"])
print(student_info["address"])

student_info["age"] = 100
print(student_info)

student_info = dict(name="Zubair", age=67, address="Pune")
print(student_info)

student_info1 = {"name": "Zubair",
                 "age": 36,
                 "office_address": "Pune",
                 "home_address": "Solapur"}

student_info2 = {"name": "Abdullah",
                 "age": 5,
                 "office_address": "Mumbai",
                 "home_address": "Pune"}

print(student_info1)
print(student_info2)