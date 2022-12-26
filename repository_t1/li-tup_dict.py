
list_keys = ['partner', 'date', 'hr', 'join', 'location', 'org', 'review', 'role', 'sbg', 'admin', 'state']
list_values = [['Infosys', 'Delloite', 'Capgemini', 'KPMG'], ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22'],
      ['Niveditha', 'bijal.shah', 'Shanya Jain', ''], ['C2H', 'permanent', 'permanent', 'permanent'],
      ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'], ['Infosys_India', '', '', 'KPMG Global Services'],
      ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore',
       'BIG DATA DEVELOPER', 'Company - KPMG Global Services'],
      ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore',
       'BIG DATA DEVELOPER', 'Job Title - Cloud Data Engineer'], ['HBT', 'SPS', 'PMT', 'PMT'],
      ['AWS data', 'AWS data', 'AWS data',
       'AWS data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse '],
      ['UAE', 'karnataka', 'MP', 'UK']]

# printing original list
print("The original key list is : " + str(list_keys))
print("The original value list is : " + str(list_values))

# Using zip() + dict() ; dict() will carry tuple key-value pairs if mapped with df_values
# Convert Tuples to Dictionary
if len(list_keys) == len(list_values):
    res = dict(zip(list_keys, list_values))

# printing result
print("Dictionary constructed from list : " + str(res))
print(res)
# op: {'partner': ['Infosys', 'Delloite', 'Capgemini', 'KPMG'], 'date': ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22'], 'hr': ['Niveditha', 'bijal.shah', 'Shanya Jain', ''], 'join': ['C2H', 'permanent', 'permanent', 'permanent'], 'location': ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'], 'org': ['Infosys_India', '', '', 'KPMG Global Services'], 'review': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Company - KPMG Global Services'], 'role': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Job Title - Cloud Data Engineer'], 'sbg': ['HBT', 'SPS', 'PMT', 'PMT'], 'admin': ['AWS data', 'AWS data', 'AWS data', 'AWS data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse '], 'state': ['UAE', 'karnataka', 'MP', 'UK']}
