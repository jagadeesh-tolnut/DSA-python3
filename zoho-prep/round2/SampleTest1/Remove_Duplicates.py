l = list(map(int,input().split(",")))
no_dup = list(set(l))
for i in range(len(no_dup),len(l)):
    no_dup.append("_")

print(*no_dup,sep=",")

