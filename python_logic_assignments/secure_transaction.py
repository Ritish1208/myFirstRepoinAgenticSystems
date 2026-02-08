balance = int(input("Balance: "))
withdrawal_amount = int(input("Withdrawal: "))
verified_input = input("Verified (True/False): ")
verified= verified_input.lower()== "true"
if verified and withdrawal_amount <=balance :
    print("Withdrawal successful")
else :
    print("Transaction denied")