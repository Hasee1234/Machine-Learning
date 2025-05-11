import pandas as pd;

# data = pd.DataFrame(
#     {
#         "Age":["18","20","21","34","24","44","13","14","15","16"],
#         "name": ["m zain azhar","m haseeb younas", "m umair tahir", "m wahaab sadiq", "m anique raza","m tahir amir","m massod ali","m faaiz zain","m hamna ali","m rimal tariq"  ],
#         "Sex":["M","M","M","M","M","M","M","M","F","F"],
#         "Marks":["56","65","78","67","44","45","67","87","90"],
#         "City": ["Gojra","satyana","lahore","fsd","paris","kamalya","karachi","peshawar","TTK","Painsra"],
#         "Date_of_birth":["2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5"],
#         "start_date":["2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5","2000-4-5"],
#         "end_date":["2024-4-5","2024-4-5","2024-4-5","2024-4-5","2024-4-5","2024-4-5","2024-4-5","2024-4-5","2024-4-5","2024-4-5"],
#     }
# )
# print("Middle Name",data["name"].str.split(" ").str.get(1))

data = pd.DataFrame(
    {
        "Age": ["18", "20", "21", "34", "24", "44", "13", "14", "15", "16"],
        "name": ["m zain azhar", "m haseeb younas", "m umair tahir", "m wahaab sadiq", "m anique raza", "m tahir amir", "m massod ali", "m faaiz zain", "m hamna ali", "m rimal tariq"],
        "Sex": ["M", "M", "M", "M", "M", "M", "M", "M", "F", "F"],
        "Marks": ["56", "65", "78", "67", "44", "45", "67", "87", "90", "50"],
        "City": ["Gojra", "satyana", "lahore", "fsd", "paris", "kamalya", "karachi", "peshawar", "TTK", "Painsra"],
        "Date_of_birth": ["2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5"],
        "start_date": ["2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5", "2000-4-5"],
        "end_date": ["2024-4-5", "2024-4-5", "2024-4-5", "2024-4-5", "2024-4-5", "2024-4-5", "2024-4-5", "2024-4-5", "2024-4-5", "2024-4-5"],
    }
)  # No comma here

print("Middle Name:",data["name"].str.split(" ").str.get(1))
data["contains_ali"] = data["name"].str.contains("ali", case=False)
print(data[["name", "contains_ali"]])
# Use replace to map each city name to its first three letters
data["City"] = data["City"].replace({city: city[:3].upper() for city in data["City"]})
print(data)

 

