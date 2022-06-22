n = int(input())

for i in range(0,n):
    for j in range(0,i+1):
        if (i+j)%2:
            print(0,end=" ")
        else:
            print(1, end=" ")
    print()



'''

5
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 

'''