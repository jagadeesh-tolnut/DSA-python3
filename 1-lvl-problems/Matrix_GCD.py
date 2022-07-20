import math

row = int(input())

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = []

for i in l1:
    for j in l2:
        l3.append(i*j)

print(math.gcd(*l3))
