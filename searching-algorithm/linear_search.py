def linear_search(Array,Key):
    pointer = 0
    while pointer < len(Array):
        if Key == Array[pointer]:
            return [True,pointer]
        else:
            pointer += 1
    return [False,"Not_Found"]
