def eq_index(arr):
    s = sum(arr) - arr[0]
    first = 0
    for i in range(len(arr)-1):
        first = first + arr[i]
        s = s - arr[i+1]
        if first == s:
            return i+1
    return -1


input_array = list(map(int,input().split()))

print(eq_index(input_array))