# Insert 0 after consecutive (K times) of 1 is found.
n = int(input())
l = list(map(int, input().split()))
k = int(input())

count = 0
final_list = []
for i in range(n):
    final_list.append(l[i])
    if l[i] == 1:
        count += 1
    else:
        count = 0

    if count == 2:
        final_list.append(0)
        count = 0

print(*final_list)

"""

i/p
12
1 0 1 1 0 1 1 0 1 1 1 1
2

o/p
1 0 1 1 0 0 1 1 0 0 1 1 0 1 1 0

"""
