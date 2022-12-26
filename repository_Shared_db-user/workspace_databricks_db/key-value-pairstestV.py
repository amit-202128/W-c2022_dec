import pandas as pd

tups = ('partner', 'date', 'hr', 'join', 'location', 'org', 'review', 'role', 'sbg', 'admin', 'state')
d = {'partner': ['Infosys', 'Delloite', 'Capgemini', 'KPMG'],
     'date': ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22'],
     'hr': ['Niveditha', 'bijal.shah', 'Shanya Jain', ''], 'join': ['C2H', 'permanent', 'permanent', 'permanent'],
     'location': ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'],
     'org': ['Infosys_India', '', '', 'KPMG Global Services'],
     'review': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore',
                'BIG DATA DEVELOPER', 'Company - KPMG Global Services'],
     'role': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore',
              'BIG DATA DEVELOPER', 'Job Title - Cloud Data Engineer'], 'sbg': ['HBT', 'SPS', 'PMT', 'PMT'],
     'admin': ['AWS data', 'AWS data', 'AWS data',
               'AWS data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse '],
     'state': ['UAE', 'karnataka', 'MP', 'UK']}


def Convert(tups, d):
    for a, b in d.items():
        d.setdefault(a, []).append(b)
        # print(a)
        # print(b)
    return d


# for i in d.items():
#     print(i)
#
# print(tups)

print(Convert(tups, d))
print(d)
# op : {'partner': ['Infosys', 'Delloite', 'Capgemini', 'KPMG'], 'date': ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22'], 'hr': ['Niveditha', 'bijal.shah', 'Shanya Jain', ''], 'join': ['C2H', 'permanent', 'permanent', 'permanent'], 'location': ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'], 'org': ['Infosys_India', '', '', 'KPMG Global Services'], 'review': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Company - KPMG Global Services'], 'role': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Job Title - Cloud Data Engineer'], 'sbg': ['HBT', 'SPS', 'PMT', 'PMT'], 'admin': ['AWS data', 'AWS data', 'AWS data', 'AWS data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse '], 'state': ['UAE', 'karnataka', 'MP', 'UK']}

data = {'partner': ['Infosys', 'Delloite', 'Capgemini', 'KPMG'],
        'date': ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22'],
        'hr': ['Niveditha', 'bijal.shah', 'Shanya Jain', ''], 'join': ['C2H', 'permanent', 'permanent', 'permanent'],
        'location': ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'],
        'org': ['Infosys_India', '', '', 'KPMG Global Services'],
        'review': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore',
                   'BIG DATA DEVELOPER', 'Company - KPMG Global Services'],
        'role': ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore',
                 'BIG DATA DEVELOPER', 'Job Title - Cloud Data Engineer'], 'sbg': ['HBT', 'SPS', 'PMT', 'PMT'],
        'admin': ['AWS data', 'AWS data', 'AWS data',
                  'AWS data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse '],
        'state': ['UAE', 'karnataka', 'MP', 'UK']}

df = pd.DataFrame(data, columns=['partner', 'date', 'hr', 'join', 'location', 'org', 'review', 'role', 'sbg', 'admin',
                                 'state'])
print(df)
