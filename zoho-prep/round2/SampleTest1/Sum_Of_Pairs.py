from itertools import combinations

arr = list(map( int,input().split(",")))
pro = int(input())
sol = []

comb = combinations(arr,2)

for i in comb:
    if sum(i) == pro:
        sol.append(i)

sol.sort()
print(*sol,sep=",")
