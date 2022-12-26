# <<<<<<< HEAD

import csv
with open("C:/Users/Amit Paul/Desktop/okk.csv", 'r') as file:
    # print(type(e))
    print("file open in read mode!")

    # read_file = e.readable()
    raw = csv.reader(file)
    data = list(raw)
    print(data)

    # operation_op_code : [['partner', 'date', 'hr', 'join', 'location', 'org', 'review', 'role', 'sbg', 'admin', 'state'], [], ['Infosys', '12-jan-22', 'Niveditha', 'C2H', 'singapore', 'Infosys_India', 'AWS Develope_Lambda_Infosys_India', 'AWS Develope_Lambda_Infosys_India', 'HBT', 'AWS data', 'UAE'], [], ['Delloite', '25-feb-21', 'bijal.shah', 'permanent', 'bangalore', 'KPMG INDIA', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'SPS', 'AWS data', 'karnataka'], [], ['First America', '16-july-22', 'Shanya Jain', 'permanent', 'gujrat', 'Delloite', 'BIG DATA DEVELOPER', 'BIG DATA DEVELOPER', 'PMT', 'AWS data', 'MP'], [], ['KPMG', '15-aug-22', '', 'permanent', 'bangalore / pune', 'KPMG Global Services', 'Company - KPMG Global Services', 'Job Title -Cloud Data Engineer', '', 'AWS data , Spark / PySpark KPMG', ''], []]
    # >>>>>>> origin/amit
    # =======

with open("C:/Users/Amit Paul/Desktop/okk.csv", 'r') as file:
    print("file open in read mode!")
    # read_file = e.readable()
    raw = csv.reader(file)
    print(raw)
    data = list(raw)
    print(data)



