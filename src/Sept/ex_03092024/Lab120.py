# Web Automation - Selenium
# Page - You are going to automate

class VWOLoginPage:

    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "zubairh@gmail.com" and self.password == "Cts-33":
            print("Allowed to Login")
        else:
            print("Not allowed to Login")

# This is the end of the class

email = input("Enter the email \n")
password = input("Enter the password \n")

vwo_obj = VWOLoginPage(email,password)
vwo_obj.login_confirm()