# Section 1 : Read numbers
numbers = []
try:
    with open("numbers.txt", "r") as data_file:
        for line in data_file:
            stripped_line = line.strip()
            if stripped_line:       #skip empty lines               
               numbers.append(int(stripped_line))
               file_status = "Filed opened successfully."
except FileNotFoundError :
    file_status = "Error: numbers.txt not found."
    numbers =[]
#Section 2 : Process the data
if numbers:
    total_numbers = len(numbers)
    sum_numbers = sum(numbers)
    average_numbers= sum_numbers / total_numbers
    processing_status = "Processing completed."
else:
    total_numbers = sum_numbers= average_numbers =0
    processing_status = "No data to Process."

#Section 3 : Log results
with open("results.log","a") as log_file :
    log_file.write(f"{file_status}\n")
    if numbers :
        log_file.write(f"Read {total_numbers} numbers.\n")
        log_file.write(f"Sum : {sum_numbers}\n")
        log_file.write(f"Average : {average_numbers}\n")
        log_file.write(f"{processing_status}\n\n") #extra newline for readability
        print(f"Read {total_numbers} numbers.")
        print(f"Sum : {sum_numbers}")
        print(f"Average : {average_numbers}")
        print(processing_status)



