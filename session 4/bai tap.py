dsnn = [-4,1,3,-16,6,8]

min_number = dsnn [0]
min_index = 0
for index, item in enumerate(dsnn):
    if min_number > item:
        min_number = item
        min_index = index

print(min_number)
print(min_index)