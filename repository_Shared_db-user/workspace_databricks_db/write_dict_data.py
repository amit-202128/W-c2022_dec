import csv

csv_columns = ['No', 'Name', 'Country']
# dict_data = [{},{},]   ## write and save to csv
dict_data = [
    {'No': 1, 'Name': 'Alex', 'Country': 'India'},
    {'No': 2, 'Name': 'Ben', 'Country': 'USA'},
    {'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
    {'No': 4, 'Name': 'Smith', 'Country': 'USA'},
    {'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
    {'No': 6, 'Name': 'Amit Kumar', 'Country': 'Russia'},
]
csv_file = "Names.csv"
try:
    with open("C:/Users/Amit Paul/Desktop/sql/output/csv/Names.csv",
            'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except Exception as msg:
    print(msg)
