list_0 = ['Amir', 'Bear', 'Charlton', 'Daman']
list_1 = ['Amir', 'Bear', 'Charlton', 'Daman']

list_2 = [1,2,3,4]

list_0.extend(list_2)
list_1.append(list_2)

print(list_0)
print(list_1)

# output dari program ini adalah :
    # list_0 = ['Amir', 'Bear', 'Charlton', 'Daman', 1, 2, 3, 4]
    # list_1 = ['Amir', 'Bear', 'Charlton', 'Daman', [1, 2, 3, 4]]