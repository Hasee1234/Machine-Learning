import pandas as pd
# #dataframe means arrangement of unstructured dataa in rows and columns
# #every column is treat as list(array in python) []
# student=pd.DataFrame(
#     {
#         "Name":["zain","zubair","faaiz"],
#         "Age":[23,34,45],
#         "class":["BS","MS","PHD"]
#     }
# )

# print(student)
# print(student["Name"])
# print(student.dtypes)
# print(student.describe())#describe tell stat or numerical things of int automatically
# print(student["Age"].max())#max points out maximum value
# print(student.info())#info tell the entries,rows,columns and memory usage

titanic=pd.read_csv("titanic.csv")
print(titanic)
print(titanic.describe())
print(titanic["Fare"].max())#i selected the fare column from titanic.csv and got maximum value of fare
print(titanic.info())
Fare=titanic["Fare"]
Fare=titanic[["Fare","Sex"]]
#.shape tells about rows and columns of that specific entity like if i add one more entity
print(Fare)
print(Fare.shape)
F1=titanic[Fare>35]
print(F1)
#you can filter values using <> these but 1st store the value in new variable

# filtering on base of location
location=titanic.iloc[3:20, 2:4]#3 to 20 rows and 2:4 means 3rd and 4 column
print(location)