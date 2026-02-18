contacts ={
    "Ravi": "9412567890",
    "Anita": "9087654321",
    "Rahul": "9876543210"
}
print("Contact Book:")
for name, number in contacts.items():
    print(name, ":", number)

search_name = input("\nEnter the name to search: ")
found = False

for name in contacts:
    if name.lower()== search_name.lower():
        print(f"{name}'s Phone number: {contacts[name]}")
        found = True
        break

if not found:
    print("Contact not found")

