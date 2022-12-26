
import csv
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import json

own_schema0 = StructType([StructField('id', StringType()),
                          StructField('ev1', StringType()),
                          StructField('ev2', StringType()),
                          StructField('ev3', StringType()),
                          StructField('date', StringType())])

own_schema1 = StructType([StructField('id', StringType()),
                          StructField('ev4', StringType()),
                          StructField('date', StringType())])

### ---------------------- execution of program starts from here ---------------------------
spark_ob = SparkSession.builder.master('local').appName('spark_json_template').getOrCreate()

### Read and store content of an Excel file
# read_file = pd.read_excel("C:/Users/Amit Paul/Desktop/book/file/Book2.xlsx")
### Write the dataframe object into csv file
# read_file.to_csv("C:/Users/Amit Paul/Desktop/book/file/Book2.csv",
#                  index=None,notepad

#                  header=True)

big_table = spark_ob.read.option('header', True). \
    option('delimiter', ',').schema(own_schema0).csv(
    "C:/Users/Amit Paul/PycharmProjects/permanent__/hive_metastore_DATASET/py_podas_2022/big_table.csv")

print(big_table)

small_table = spark_ob.read.option('header', True). \
    option('delimiter', ',').schema(own_schema1).csv(
    "C:/Users/Amit Paul/PycharmProjects/permanent__/hive_metastore_DATASET/py_podas_2022/small_table.csv")

print(small_table)

# """ merge two dataframe for schema columns
""" DATAFRAME_COLUMNS_SCHEMA"""
big_table.createTempView("big_tbl")
small_table.createTempView("small_tbl")

print(big_table.show())
print(small_table.show())

""" JDBC_template_schema """
big_tbl_view = spark_ob.sql("select id, ev1 ,ev2 , ev3 , date from big_tbl")
rdd_df = big_tbl_view.rdd
dataframe_to_rdd = rdd_df
dataframe_to_rdd.map(lambda x: type(x))
row_type_rdd_to_dataframe = spark_ob.createDataFrame(dataframe_to_rdd, own_schema0)
row_type_rdd_to_dataframe.createTempView("big_table")
big_table_view = spark_ob.sql("select id, (ev1 ,ev2 , ev3) as event , date from big_table")
big_table_view.toDF("id", "event", "date")
big_table_view.createOrReplaceTempView("ff2")
big_table_view = spark_ob.sql("select small_tbl.id, small_tbl.ev4 as event, small_tbl.date from small_tbl join ff2 on small_tbl.id = ff2.id")

## print(big_table_view.__dict__)
print(big_table_view.printSchema())
other =  big_table_view
print(big_table_view.union(other))
#
try:
    df_columns = {}
    total_col = 0
    total_col = int(input("Enter total no. of column:\n "))
    for i in range(total_col):
        column_key = int(input("Enter column key:\n "))
        column_value = input("Enter column value:\n   ")
        df_columns[column_key] = column_value
        total_col -= 1
    print(df_columns)
    d = {}
    d = df_columns.values()
    lst = eval(input("Input list of array"))
    dct = {}
    row_index = 0
    for c in d:
        dct[c] = lst[row_index]
        row_index += 1
    print(dct)

except Exception as err_msg:
    print(err_msg)

own_schema2 = StructType([StructField('car_company', IntegerType()), StructField('car_model', StringType()),
                              StructField('price', StringType()), StructField('units_per_annum', StringType()),
                              StructField('dealer_commission', StringType())])

""" dataframe_schema """

qu_scrn = "table_view.csv"

df1 = spark_ob.read.option('header', True).option('delimeter', ',').schema(own_schema2).csv(
        'C:/Users/Amit Paul/Desktop/cars_bhk.csv')
df1.createTempView("file_f2")
df1.printSchema()
df2_result = spark_ob.sql("select * from file_f2")
df2_result.show()
rdd2 = df2_result.rdd
dataframe_to_rdd = df2_result.rdd
dataframe_to_rdd.map(lambda x: type(x))
row_type_rdd_to_dataframe = spark_ob.createDataFrame(dataframe_to_rdd, own_schema2)
rot_rdd = row_type_rdd_to_dataframe
df_columns_p = rot_rdd.toJSON()
df_columns_prod = pd.DataFrame.from_dict(dct)
df_jsondataframe_schema = json.dumps(dct, sort_keys=True, indent=4)
print(df_jsondataframe_schema)


csv_columns = ['No', 'Name', 'Country']
# dict_data = [{},{},]   ## write and save to csv
dict_data = [
    {'No': 1, 'Name': 'Alex', 'Country': 'India'},
    {'No': 2, 'Name': 'Ben', 'Country': 'USA'},
    {'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
    {'No': 4, 'Name': 'Smith', 'Country': 'USA'},
    {'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
    {'No': 6, 'Name': 'Amit Kumar', 'Country': 'Russia'},
]
csv_file = "Names.csv"
try:
    with open("C:/Users/Amit Paul/Desktop/sql/Names.csv",
            'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except Exception as msg:
    print(msg)
