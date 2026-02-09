correct_password= "admin123"
password =""
while password != correct_password:
    password =input("Enter password: ")
    if password != correct_password:
        print("Incorrect Password. Try Again!")
print("Access granted")