def check(num):
    if num%2 ==0:
        return "Number is Even"
    else:
        return "Number is Odd"
    
#Take input from the user
n= int(input("Enter a number: "))
#Call the function and store the result
res = check(n)
#print the result
print(res)
