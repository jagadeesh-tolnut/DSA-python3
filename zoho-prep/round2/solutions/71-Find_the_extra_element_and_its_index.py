l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

index = 0
for i in l1:
    if i not in l2:
        print(f"{i} is the extra element in array 1 at index {index}")
    index += 1

index = 0
for i in l2:
    if i not in l1:
        print(f"{i} is the extra element in array 2 at index {index}")
    index += 1


'''

i/p
10 20 30 12 5
10 5 30 20

o/p
12 is the extra element in array 1 at index 3

'''
