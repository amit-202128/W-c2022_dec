import pandas as pd
import csv

filename = "C:/Users/Amit Paul/OneDrive/Desktop/folder/bin/file-c.csv"
def read_csv(filename):
    filename = "C:/Users/Amit Paul/OneDrive/Desktop/folder/bin/file-c.csv"

    with open(filename) as f:
        file_data=csv.reader(f)
        headers=next(file_data)
        d = [dict(zip(headers, i)) for i in file_data]
        return d

print(read_csv(filename))
print()
# op :
# [{'partner': 'Infosys', 'date': '12-Jan-22', 'hr': 'Niveditha', 'join': 'C2H', 'location': 'singapore', 'org': 'Infosys_India', 'review': 'AWS Develope_Lambda_Infosys_India', 'role': 'AWS Develope_Lambda_Infosys_India', 'sbg': 'HBT', 'admin': 'AWS data', 'state': 'UAE'},
#  {'partner': 'Delloite', 'date': '25-Feb-21', 'hr': 'bijal.shah', 'join': 'permanent', 'location': 'bangalore', 'org': '', 'review': 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'role': 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'sbg': 'SPS', 'admin': 'AWS data', 'state': 'karnataka'},
#  {'partner': 'Capgemini', 'date': '16-Jul-22', 'hr': 'Shanya Jain', 'join': 'permanent', 'location': 'gujrat', 'org': '', 'review': 'BIG DATA DEVELOPER', 'role': 'BIG DATA DEVELOPER', 'sbg': 'PMT', 'admin': 'AWS data', 'state': 'MP'},
#  {'partner': 'KPMG', 'date': '15-Aug-22', 'hr': 'Sagar', 'join': 'permanent', 'location': 'bangalore / pune', 'org': 'KPMG Global Services', 'review': 'Company - KPMG Global Services', 'role': 'Job Title -Cloud Data Engineer', 'sbg': 'PMT', 'admin': 'AWS data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse', 'state': 'USA'}
# ]

# initialising _dictionary
initial_dict = {'partner': ['Infosys', '', '', 'KPMG'], 'date': ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22'],
                'hr': ['Niveditha', '\xa0bijal.shah', 'Shanya Jain', ''],
                'join': ['C2H', 'permanent', 'permanent', 'permanent'],
                'location': ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'],
                'org': ['Infosys_India', '', '', 'KPMG Global Services'],
                'review': ['AWS Develope_Lambda_Infosys_India',
                           'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER',
                           'Company - KPMG Global Services'], 'role': ['AWS Develope_Lambda_Infosys_India',
                                                                       'Big Data / Pyspark Development - Leading Co. - Bangalore',
                                                                       'BIG DATA DEVELOPER',
                                                                       'Job Title -\xa0Cloud\xa0Data\xa0Engineer'],
                'sbg': ['HBT', 'SPS', 'PMT', ''], 'admin': ['AWS\xa0data', 'AWS\xa0data', 'AWS\xa0data',
                                                          'AWS\xa0data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse '],
                'state': ['UAE', 'karnataka', 'MP', '']}

# list of name, degree, score
part = ['Infosys', 'Delloite', 'Capgemini', 'KPMG']
dt = ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22']
ho = ['Niveditha', 'bijal.shah', 'Shanya Jain', 'Sagar']
jo = ['C2H', 'permanent', 'permanent', 'permanent']
loc = ['singapore', 'bangalore', 'gujrat', 'bangalore / pune']
og = ['Infosys_India', '', '', 'KPMG Global Services']
rev = ['AWS Develope_Lambda_Infosys_India',
                           'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER',
                           'Company - KPMG Global Services']
rol = ['AWS Develope_Lambda_Infosys_India','Big Data / Pyspark Development - Leading Co. - Bangalore','BIG DATA DEVELOPER','Job Title -Cloud Data Engineer']
sb = ['HBT', 'SPS', 'PMT', 'PMT']
ad = ['AWS data', 'AWS data', 'AWS data','AWS data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse']
st = ['UAE', 'karnataka', 'MP', 'USA']

# dictionary of lists
dict = {'partner': part, 'date': dt, 'hr': ho, 'join': jo, 'location': loc, 'org':og, 'review': rev, 'role': rol, 'sbg': sb, 'admin': ad, 'state': st}

df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('C:/Users/Amit Paul/OneDrive/Desktop/folder/bin/file-d.csv')






# printing initial_dictionary
print("intial_dictionary", str(initial_dict))

# split dictionary into keys and values
keys = initial_dict.keys()
values = initial_dict.values()

# printing keys and values separately
print("keys : ", str(keys))
print("values : ", str(values))


print()
# list of values from dictionary
li = list(initial_dict.values())
print(li)

# keys = ['partner', 'date', 'hr', 'join', 'location', 'org', 'review', 'role', 'sbg', 'admin', 'state']

# get list of values using map
value = list(map(initial_dict.get, keys))

print(value)