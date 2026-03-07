import pandas as pd

#Sample dataset creation
data= {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Arjun", "Simran", "Rahul", "Priya", "Vikram", "Anita"],
    "Age": [21, 22, 23, 24, 22, 21, 23, 25, 22, 24],
    "Score": [89, 78, 92, 88, 76, 95, 81, 29,90,84],
    "Label": ["Pass","Pass", "Pass", "Pass","Pass", "Pass", "Pass", "Fail","Pass","Pass" ]

}
df_sample = pd.DataFrame(data)

#Save dataset to CSV
df_sample.to_csv("dataset.csv", index=False)

print("Sample Dataset created and saved as dataset.csv\n")

df = pd.read_csv("Dataset.csv")

print("First 5 rows:")
print(df.head(), "\n")

print("Last 5 rows:")
print(df.tail(), "\n")

print("Dataset Information: ")
print(df.info(), "\n")

print("Summary Statistics:")
print(df.describe(), "\n")

age_column= df["Age"]
print("Single Column Selected (Age): ")
print(age_column, "\n")

selected_col =df[["Name", "Score"]]
print("Multiple Columns Selected (Name and Score): ")
print(selected_col, "\n")

fil_rows= df[df["Score"]>80]
print ("Filtered Rows (Score > 80): ")
print(fil_rows)
