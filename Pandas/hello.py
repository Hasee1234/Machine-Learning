import pandas as pd;

# air = pd.read_csv("air.csv")

# print(air.describe())

# hello = air.agg(
#     {
#         "station_paris" : ["max","min"],
#         "station_london" :         ["max" ,"min", "skew","median"]
#     }
# )
# print(hello)
# titanic=pd.read_csv("titanic.csv")
# print(titanic["Name"].str.split("").str.get(1))

# print(titanic[titanic["Name"].str.contains('Mr')])

stu=pd.DataFrame(
    {
        "Name":["Mr Haseeb Mirza","Mr faaiz Ansar","Mr Zain Azhar","Mr Abdullah Naeem","Mr Zubair Shehzad"],
        "Age":[20,21,22,19,18],
        "Marks":[90,89,91,83,88]
    }
)
print(stu["Name"].str.split(" ").str.get(1))