n  = int(input())
temp = []
temp_list = [1, 1]

for i in range(1,n+1):
    print(" "*(n-i),end="")
    if i==1 or i==2:
        print("1 "*i)
    else:
        temp = []
        temp.append(1)
        for k in range(1,len(temp_list)):
            temp.append(temp_list[k-1]+temp_list[k])
        temp.append(1)
        temp_list = temp.copy()
        print(*temp_list)
