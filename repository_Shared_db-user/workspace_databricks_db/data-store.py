import csv

with open("C:/Users/Amit Paul/OneDrive/Desktop/partner_role/name/permanent/file-c.csv", 'r') as file:
    # print(type(e))
    print("file open in read mode!")
    # read_file = e.readable()
    raw = csv.reader(file)
    data = list(raw)
    print(data)

# op : [['partner', 'date', 'hr', 'join', 'location', 'org', 'review', 'role', 'sbg', 'admin', 'state'], [], ['Infosys', '12-jan-22', 'Niveditha', 'C2H', 'singapore', 'Infosys_India', 'AWS Develope_Lambda_Infosys_India', 'AWS Develope_Lambda_Infosys_India', 'HBT', 'AWS data', 'UAE'], [], ['Delloite', '25-feb-21', 'bijal.shah', 'permanent', 'bangalore', 'KPMG INDIA', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'Big Data / Pyspark Development - Leading Co. - Bangalore', 'SPS', 'AWS data', 'karnataka'], [], ['First America', '16-july-22', 'Shanya Jain', 'permanent', 'gujrat', 'Delloite', 'BIG DATA DEVELOPER', 'BIG DATA DEVELOPER', 'PMT', 'AWS data', 'MP'], [], ['KPMG', '15-aug-22', '', 'permanent', 'bangalore / pune', 'KPMG Global Services', 'Company - KPMG Global Services', 'Job Title -Cloud Data Engineer', '', 'AWS data , Spark / PySpark KPMG', ''], []]


l = ['partner', 'date', 'hr', 'join', 'location', 'org', 'review', 'role', 'sbg', 'admin', 'state']
for i in range(len(l)):
    print(l[i], [i])

print()
l = sorted(l)

l = list(filter(str.strip,l))
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<=l[j]:
#             l[i],l[j] = l[j],l[i]
print(l)
