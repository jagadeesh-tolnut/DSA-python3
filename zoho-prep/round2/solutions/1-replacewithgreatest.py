arr = list(map(int,input().split()))
l=len(arr)

for i in range(l):
    if i == l-1:
        arr[i] = -1
    else:
        arr[i] = max(arr[i+1:])

print(arr)