if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    first = []
    final = []
    for i in range(0, x + 1):
        for j in range(0, y + 1):  # any idea? # aama #logic la mistake # crtu
            for k in range(0, z + 1):
                temp = [i, j, k]
                first.append(temp)
    # print(first)
    for l in first:
        if sum(l) != n:
            final.append(l)
    print(final)
