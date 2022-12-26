# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
li = list(filter(lambda x: (x % 2 == 0), li))
print('By using filter :', li)

list_remove = [5, [(1, 'amit'), (2, 'pawn'), (3, 'rohan')], 7, 22, 97, 54, 62, 77, 23, 73, 61]
list_remove = list(filter(lambda x: (x == [(1, 'amit'), (2, 'pawn'), (3, 'rohan')]), list_remove))
print('By using filter :', list_remove)
new_tup = tuple(list_remove)
print("")
print(new_tup)
