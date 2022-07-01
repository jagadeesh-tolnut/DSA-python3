l = list(map(int,input().split(",")))
no_dup = list(set(l))
for i in range(len(no_dup),len(l)):
    no_dup.append("_")

print(*no_dup,sep=",")

'''

0,0,1,1,1,2,2,3,3,4
0,1,2,3,4,_,_,_,_,_

'''