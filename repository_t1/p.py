import json
import pandas as pd
# from pandas import DataFrame

json_data = {
    "client": [
        "Infosys",
        "",
        "",
        "KPMG"
    ],
    "date": [
        "12-jan-22",
        "25-feb-21",
        "16-july-22",
        "15-aug-22"
    ],
    "hr": [
        "Niveditha",
        "\u00a0bijal.shah",
        "Shanya Jain",
        ""
    ],
    "join": [
        "C2H",
        "permanent",
        "permanent",
        "permanent"
    ],
    "location": [
        "singapore",
        "bangalore",
        "gujrat",
        "bangalore / pune"
    ],
    "org": [
        "Infosys_India",
        "",
        "",
        "KPMG Global Services"
    ],
    "review": [
        "AWS Develope_Lambda_Infosys_India",
        "Big Data / Pyspark Development - Leading Co. - Bangalore",
        "BIG DATA DEVELOPER",
        "Company - KPMG Global Services"
    ],
    "role": [
        "AWS Develope_Lambda_Infosys_India",
        "Big Data / Pyspark Development - Leading Co. - Bangalore",
        "BIG DATA DEVELOPER",
        "Job Title -\u00a0Cloud\u00a0Data\u00a0Engineer"
    ],
    "sbg": [
        "HBT",
        "SPS",
        "PMT",
        ""
    ],
    "admin": [
        "AWS\u00a0data",
        "AWS\u00a0data",
        "AWS\u00a0data",
        "AWS\u00a0data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse "
    ],
    "state": [
        "UAE",
        "karnataka",
        "MP",
        ""
    ]
}
print(json.dumps(json_data, sort_keys=True, indent=4))

df_json = json.dumps(json_data, sort_keys=True, indent=4)
print(df_json)
path = 'C:/Users/Amit Paul/PycharmProjects/Project_a/sql/sql/output/json/json/company-data.json'
# opens the JSON file
with open("C:/Users/Amit Paul/PycharmProjects/Project_a/sql/sql/output/json/company-data.json") as json_file:
    data = json.load(json_file)

# type of data variable
print("Type:", type(data))

# prints the data in dictionary
print("client:", data['client'])
print("date:", data['date'])
print("hr:", data['hr'])
print("join:", data['join'])
print("location:", data['location'])
print("org:", data['org'])
print("review:", data['review'])
print("role:", data['role'])
print("sbg:", data['sbg'])
print("admin:", data['admin'])
print("state:", data['state'])


def writeToJSONFile(path, json_data):
    path = 'C:/Users/Amit Paul/PycharmProjects/Project_a/sql/sql/output/json/c-data.json'
    with open(path, 'w') as json_file:
        json.dump(json_data, json_file)


writeToJSONFile(path, json_data)
try:
    df_data = json.loads(json_data)
    print(df_data)

except Exception as msg:
    print(msg)
