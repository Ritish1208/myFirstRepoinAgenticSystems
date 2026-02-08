age = int(input("Age: "))
has_id_input = input("Has ID (True/False): ")
has_id = has_id_input.lower() == "true"
if age >= 18 and has_id :
    print("Entry Allowed")
else :
    print("Entry Denied")