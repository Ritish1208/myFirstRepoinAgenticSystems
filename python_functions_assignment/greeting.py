# A function defined with a parameter 'name'
def greet(name):
    return f"Hello, {name}!"
#Take input from user
user = input("Enter your name: ")
#call the function with user input
message = greet(user)
#print the message
print(message)