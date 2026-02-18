emp_id= int(input("Enter Employee ID: "))
emp_name= input("Enter Employee Name: ")
emp_department = input("Enter Department: ")

employee =(emp_id, emp_name, emp_department)

roles= set()
num_roles = int(input("\nHOw many roles does the employee have? "))
for i in range(num_roles):
    role = input(f" Enter role {i+1}: ").lower()
    roles.add(role)

print("\n==========Employee Details==========")
print(f"Employee ID     : {employee[0]}")
print(f"Employee Name   : {employee[1]}")
print(f"Department      : {employee[2]}")
print(f"Assigned Roles  : {','.join(roles)}")

print("\n==========Admin Access Verification==========")
if "admin" in roles:
    print("Admin access     : Yes")
else:
    print("Admin access     : No")