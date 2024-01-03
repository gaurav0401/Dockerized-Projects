def print_square(n):
    for i in range(n):
        for j in range(n):
            if (i==0 or i==n-1):
                print('*',end=' ')
            elif ((i>0 and j==0) or (i>0 and j==n-1)):
                 print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


print_square(8)