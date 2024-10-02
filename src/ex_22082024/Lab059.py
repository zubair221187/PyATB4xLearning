# Match Statement
# Same as Switch in Java
# match the O/P and execute
# Works in Python > 3.10

# match variable:
#     case pattern1:
#         # code block
#
#     case pattern2:
#         # code block

# Write a program to ask the user which browser he want to run automation

browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox Code")
    case "chrome":
        print("Execute the Chrome Code")
    case "edge":
        print("Execute the Edge Code")
    case "safari":
        print("Execute the Safari Code")
    case _:
        print("Browser Not Found !")