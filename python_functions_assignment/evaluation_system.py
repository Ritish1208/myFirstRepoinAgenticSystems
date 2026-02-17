#Function 1 - greeting the student
def greet_student(name):
    return f"Hello, {name}"
#Function 2- Calculation of number of subjects and average score
def calculate_average(scores):
    num_subjects = len(scores)
    avg_score = sum(scores)/ num_subjects if num_subjects >0 else 0 
    return num_subjects, avg_score
#Function 3 - Determine pass or fail
def evaluate_result(avg_score):
    if avg_score >= 50:
        return "Pass"
    else :
        return "Fail"    
#Function 4 - Main function 
def main():
    #take input for student name
    student_name = input("Enter Student's Name: ")
    #Take input for scores 
    scores_input = input("Enter scores seperated by spaces: ")
    scores= [float(score) for score in scores_input.split()]
    
    greeting = greet_student(student_name)
    num_subjects, avg_score = calculate_average(scores)
    result = evaluate_result(avg_score)

    print(f"{greeting}")
    print(f"Subjects: {num_subjects}")
    print(f"Average Score: {avg_score:.1f}")
    print(f"Result: {result}")
    
main()

