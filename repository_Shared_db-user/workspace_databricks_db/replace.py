sample_dict = {'client': ['Infosys', '', '', 'KPMG'], 'date': ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22'], 'hr': ['Niveditha', '\xa0bijal.shah', 'Shanya Jain', ''], 'join': ['C2H', 'permanent', 'permanent', 'permanent'], 'location': ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'], 'org': ['Infosys_India', '', '', 'KPMG Global Services'], 'review': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Company - KPMG Global Services'], 'role': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Job Title -\xa0Cloud\xa0Data\xa0Engineer'], 'sbg': ['HBT', 'SPS', 'PMT', ''], 'sct': ['AWS\xa0data', 'AWS\xa0data', 'AWS\xa0data', 'AWS\xa0data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse '], 'state': ['UAE', 'karnataka', 'MP', '']}
# Converting into list of tuple
# method 1:
list_of_tuples = list(sample_dict.items())
print(list_of_tuples)

# # method 2:
# list = [(k, v) for k, v in sample_dict.items()]
# print(list)

# import copy
# # deep copy
# l_d = copy.deepcopy(list)
# print(l_d)
#
# # shallow copy


## op : [('client', ['Infosys', '', '', 'KPMG']), ('date', ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22']), ('hr', ['Niveditha', '\xa0bijal.shah', 'Shanya Jain', '']), ('join', ['C2H', 'permanent', 'permanent', 'permanent']), ('location', ['singapore', 'bangalore', 'gujrat', 'bangalore / pune']), ('org', ['Infosys_India', '', '', 'KPMG Global Services']), ('review', ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Company - KPMG Global Services']), ('role', ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Job Title -\xa0Cloud\xa0Data\xa0Engineer']), ('sbg', ['HBT', 'SPS', 'PMT', '']), ('sct', ['AWS\xa0data', 'AWS\xa0data', 'AWS\xa0data', 'AWS\xa0data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse ']), ('state', ['UAE', 'karnataka', 'MP', ''])]
