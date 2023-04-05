rows = 7
for i in range(1, rows + 1):  
    for j in range(1, rows + 1):  
        # Check condition if value of j is smaller or equal than  
        # the j then print i otherwise print j  
        if j <= i:  
            print(j, end=' ')  
        else:  
            print('*', end=' ')  
    print()