import csv
csv_columns = ['review', 'date', 'sbg', 'role', 'join', 'location', 'state', 'hr', 'admin', 'org', 'client']
dict_data = []

# [{},{},{}]

# # multidimentional_list_of_values
# dict_data = [['Infosys', '', '', 'KPMG'], ['12-jan-22', '25-feb-21', '16-july-22', '15-aug-22'], ['Niveditha', '\xa0bijal.shah', 'Shanya Jain', ''], ['C2H', 'permanent', 'permanent', 'permanent'], ['singapore', 'bangalore', 'gujrat', 'bangalore / pune'], ['Infosys_India', '', '', 'KPMG Global Services'], ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Company - KPMG Global Services'], ['AWS Develope_Lambda_Infosys_India', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'BIG DATA DEVELOPER', 'Job Title -\xa0Cloud\xa0Data\xa0Engineer'], ['HBT', 'SPS', 'PMT', ''], ['AWS\xa0data', 'AWS\xa0data', 'AWS\xa0data', 'AWS\xa0data , Spark or PySpark , Hive , Big Data , Python , Scala , SQL , Data lake , data warehouse '], ['UAE', 'karnataka', 'MP', '']]

csv_file = "2021-.csv"

try:
    with open("C:/Users/Amit Paul/PycharmProjects/Project_a/sql/sql/output/csv/2021-.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except Exception as msg:
    print(msg)
