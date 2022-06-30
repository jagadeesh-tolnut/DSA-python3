def binary_search(Array, Key):
    low = 0
    high = len(Array)-1
    while low <= high :
        mid = (low + high) // 2
        if Array[mid] == Key:
            return [True,mid]
        elif Array[mid] > Key:
            high = mid - 1
        else:
            low = mid + 1
    return [False,"Not_found"]