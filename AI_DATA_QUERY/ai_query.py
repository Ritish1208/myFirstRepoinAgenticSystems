import pandas as pd

#Load dataset
df= pd.read_csv("students.csv")
print("Original Dataset : ")
print(df)
print()


#Select a single column
print("Scores column : ")
print(df["Score"])
print()

#Select multiple columns
name_score_df =df[["Name", "Score"]]
print("Name and score DataFrame :")
print(name_score_df)
print()

#USing iloc
print("First Three rows using iloc:")
print(df.iloc[0:3])
print()

#Set name as index an use loc
df_index= df.set_index("Name")
print("Using iloc after setting name as index: ")
print(df_index.loc["Alice"])
print()

#Filter score>85
high_scores =df[df["Score"]>85]
print("Student with score >85:")
print(high_scores)
print()

#Filter scores>85 and passed
high_passed =df[(df["Score"]>85) & (df["Passed"]== True)]
print("Students with Score > 85 AND Passed: ")
print(high_passed)
print()

#SOrt descending
sorted_Students= high_passed.sort_values(by ="Score", ascending=False)
print("Sorted by Score(Descending):")
print(sorted_Students)
print()

#Chaining Filtering + sorting
chained_result = df[(df["Score"]>85)& (df["Passed"]== True)] \
      .sort_values(by="Score", ascending=False)

print("High Performing Students :")
print(chained_result[["Name", "Score"]])

