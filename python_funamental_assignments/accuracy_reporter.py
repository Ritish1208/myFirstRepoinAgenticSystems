try:
    accuracy = float(input("Enter model accuracy :"))
    print(f"Model accuracy is {accuracy}")
except ValueError:
    print("Please enter a numeric value")