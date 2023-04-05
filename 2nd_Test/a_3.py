list_1=['Amir','Bear','Charlton','Daman']
list_2=list_1
list_3=list_1[:]

list_1[0]='Alice'
list_2[3]='Kevin'
list_3[1]='Bob'

print(list_1)
print(list_2)
print(list_3)

# output dari program ini adalah :
    # list_1 = ['Alice', 'Bear', 'Charlton', 'Kevin']
    # list_2 = ['Alice', 'Bear', 'Charlton', 'Kevin']
    # list_3 = ['Amir', 'Bob', 'Charlton', 'Daman']