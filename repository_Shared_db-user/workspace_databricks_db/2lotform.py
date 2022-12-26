# Initialization of dictionary
dict = {'client': ['Infosys', 'KPI', 'EY', 'KPMG'], 'date': ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22'],
        'hr': ['Niveditha', 'bijal.shah', 'Shanya Jain', ''],
        'join': ['C2H', 'permanent', 'permanent', 'permanent'],
        'location': ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'],
        'org': ['Infosys_India', '', '', 'KPMG Global Services'],
        'review': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore',
                   'BIG DATA DEVELOPER', 'Company - KPMG Global Services'],
        'role': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore',
                 'BIG DATA DEVELOPER', 'Job Title -Cloud Data Engineer'], 'sbg': ['HBT', 'SPS', 'PMT', ''],
        'sct': ['AWS data', 'AWS data', 'AWS data',
                'AWS data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse '],
        'state': ['UAE', 'karnataka', 'MP', '']}

# Converting into list of tuple using list comprehension
# method 1
list = [(k, v)
        for k, v in dict.items()]
# Printing list of tuple
print(list)

#

# converting to list of tuple
# method 2
dict_list = [tuple(val)
             for dic in dict
             for key, val in dict.items()]

# printing result
print("Resultant list of tuples: {}".format(dict_list))

#