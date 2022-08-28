T = int(input())

for i in range(T):
    tests = []
    sol = ""
    n,m = map(int,input().split())
    x,y = map(int,input().split())
    for i in range(n):
        tests.append(input())
    for i in tests:
        F = 0
        P = 0
        for j in i:
            if j == "F":
                F += 1
            elif j == "P":
                P += 1
        if F >= x:
            sol += "1"
        elif F >= x-1 and P >= y:
            sol += "1"
        else:
            sol += "0"
    print(sol)
