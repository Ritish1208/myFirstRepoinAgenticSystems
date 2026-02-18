marks=[]
#Taking input from 8 students
print("Enter marks for 8 students")
for i in range(8):
    mark= int(input(f"Enter mark for student {i+1}: "))
    marks.append(mark)

#Display Full list
print("\nFull List of Marks: ", marks)

#List slicing
print("First three marks: ", marks[:3])
print("Last three marks:", marks[-3:])

#calculations
highest = max(marks)
lowest = min(marks)
average = sum(marks)/ len(marks)

#Display results
print("Highest:", highest)
print("Lowest", lowest)
print("Average", round(average, 2))