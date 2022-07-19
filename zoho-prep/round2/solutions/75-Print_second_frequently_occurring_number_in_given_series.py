import collections

l = list(map(int,input().split()))

c = collections.Counter(l)

num = list(c.keys())
num.sort()
print(num[1])


'''

i/p
1 1 2 3 1 2 4

o/p
2

'''