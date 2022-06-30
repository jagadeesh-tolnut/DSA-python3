def binary_search(Array, Key , low, high):
    if low > high:
        return [False,"Not_found"]
    else:
        mid = (low+high) // 2
        if Array[mid] == Key:
            return [True,mid]
        elif Array[mid] > Key:
            return binary_search(Array, Key , low, mid-1)
        else:
            return binary_search(Array, Key , mid+1, high)