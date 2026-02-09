total =0
print("Enter numbers to add. Enter 0 to stop.")
while True:
    num = int(input("Enter a number: "))
    if num==0:
        break
    total += num 

print("Total: ", total)