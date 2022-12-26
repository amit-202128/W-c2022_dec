# firewall lambda handler -- convert list to tuple then convert into dict first then

# initializing tuples
# test_tup1 = ('GFG', 'is', 'best')
# test_tup2 = (1, 2, 3)

list_keys = [1, 2, 3, 4, 5]
list_values = ['blue', 'green', 'red', 'yellow', 'orange']

# printing original list
print("The original key list is : " + str(list_keys))
print("The original value list is : " + str(list_values))

# Using zip() + dict() ; dict() will carry tuple key-value pairs if mapped with df_values
# Convert Tuples to Dictionary
if len(list_keys) == len(list_values):
    res = dict(zip(list_keys, list_values))

# printing result
print("Dictionary constructed from list : " + str(res))

