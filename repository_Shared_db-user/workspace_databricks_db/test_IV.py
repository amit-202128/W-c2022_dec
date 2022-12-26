# # op:for a array value of a key
#
# x = {'partner': ['Infosys', 'Delloite', 'Capgemini', 'KPMG'],
#                'date': ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22'],
#                'hr': ['Niveditha', 'bijal.shah', 'Shanya Jain', ''],
#                'join': ['C2H', 'permanent', 'permanent', 'permanent'],
#                'location': ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'],
#                'org': ['Infosys_India', '', '', 'KPMG Global Services'], 'review': ['AWS Develope_Lambda_Infosys_India',
#                                                                                     'Big Data / Pyspark Development - Leading Co. - Bangalore',
#                                                                                     'BIG DATA DEVELOPER',
#                                                                                     'Company - KPMG Global Services'],
#                'role': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore',
#                         'BIG DATA DEVELOPER', 'Job Title - Cloud Data Engineer'], 'sbg': ['HBT', 'SPS', 'PMT', 'PMT'],
#                'admin': ['AWS data', 'AWS data', 'AWS data',
#                          'AWS data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse '],
#                'state': ['UAE', 'karnataka', 'MP', 'UK']}

import csv
# each row is in the form {k1 : v1, ... kn : vn}


# [{"key0": "0"}, {"key1": "1"},...]

names_c = ['0','1']
samples = []
h = []
print(type(samples))

# {'partner': ['KPMG', 'Infosys', 'Delloite', 'First America'], 'date': ['12-Jan-22', '25-Feb-21', '16-Jul-22', '15-Aug-22'], 'hr': ['Niveditha', 'bijal.shah', 'Shanya Jain', 'Shankar'], 'join': ['C2H', 'permanent', 'permanent', 'permanent'], 'location': ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'], 'org': ['Infosys_India', 'KPMG INDIA', 'Delloite', 'KPMG Global Services'], 'review': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Company - KPMG Global Services'], 'role': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Job Title -Cloud Data Engineer'], 'sbg': ['HBT', 'SPS', 'PMT', ''], 'admin': ['AWS data', 'AWS data', 'AWS data', 'AWS data , Spark / PySpark KPMG'], 'state': ['UAE', 'karnataka', 'MP', 'Singapore']}

for index_i in range(len(names_c)):   # index_i --> 0 , 1 , 2 , 3
    samples_dict = {"key0":None, "key1": None}
    samples_dict["key0"] = names_c[index_i]
    samples_dict["key1"] = index_i
    samples.append(samples_dict)
    h.append(samples_dict["key0"])

print(samples)
print(h)


columns = []
# columns = names_c
out_path_file= "C:/Users/Amit Paul/OneDrive/Desktop/folder/bin/0_pd.csv"
with open(out_path_file,'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if columns:
            for i, value in enumerate(row):
                columns[i].append(value)
        else:
            # first row
            columns = [[value] for value in row]

# you now have a column-major 2D array of your file.
as_dict = {c[0] : c[1:] for c in columns}
print(as_dict)

# op : {'partner': ['KPMG', 'Infosys', 'Delloite', 'First America'], 'date': ['12-Jan-22', '25-Feb-21', '16-Jul-22', '15-Aug-22'], 'hr': ['Niveditha', 'bijal.shah', 'Shanya Jain', ''], 'join': ['C2H', 'permanent', 'permanent', 'permanent'], 'location': ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'], 'org': ['Infosys_India', 'KPMG INDIA', 'Delloite', 'KPMG Global Services'], 'review': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Company - KPMG Global Services'], 'role': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Job Title -Cloud Data Engineer'], 'sbg': ['HBT', 'SPS', 'PMT', ''], 'admin': ['AWS data', 'AWS data', 'AWS data', 'AWS data , Spark / PySpark KPMG'], 'state': ['UAE', 'karnataka', 'MP', 'UK']}


# import csv
# # each row is in the form {k1 : v1,
# #                      ... kn : vn}
# # list_of_dicts = [{'hello': 'goodbye'},
# #                  {'yes': 'no'}]
# list_of_dicts = [{'key0': 'column_0', 'key1': [0]},
#                  {'key0': 'columm_1', 'key1': [1]}]
