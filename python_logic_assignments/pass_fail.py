try:
    score = int(input("Enter the score: "))
    if score >=50 :
       print("Pass")
    else :
       print("Fail")
except ValueError:
   print("Invalid input, Please enter an integer score")
