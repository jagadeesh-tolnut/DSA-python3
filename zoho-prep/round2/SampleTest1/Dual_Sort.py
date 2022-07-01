l = list(map(int,input().split(",")))
l.sort()

br = len(l) - len(l)//2 - 1

odd = l[:br+1]
even = l[br+1:]
even.sort(reverse = True)
main_list = []

for i in range(len(odd)):
    main_list.append(odd[i])
    if len(even) > i:
        main_list.append(even[i])

print(*main_list,sep=",")
