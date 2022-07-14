# sort 0,1,2 in a array without using sorting algorithm and copying array
# TC : O(n)

a = list(map(int,input().split()))
l = 0
m = 0
h = len(a)-1

while(m<h):
    if a[m] == 0:
        a[l],a[m] = a[m],a[l]
        l += 1
        m += 1
    elif a[m] == 2:
        a[m],a[h] = a[h],a[m]
        h -= 1
    elif a[m] == 1:
        m += 1

print(*a)



"""

i/p
1 0 2 0 1 0 2

o/p
0 0 0 1 1 2 2

"""