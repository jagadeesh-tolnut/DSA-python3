def findtime(time, n, b, m):
    if n == 1:
        return m * 1
    if n % 2 == 0:
        p = n // 2
    else:
        p = (n + 1) // 2
    time = time + (p * m) + b
    m = 2 * m
    n = n - p
    if n != 0:
        return findtime(time, n, b, m)
    else:
        return int(time-b)

testcase = int(input())
for _ in range(testcase):
    time = 0
    n, b, m = map(int, input().split())
    totaltime = findtime(time,n,b,m)
    print(totaltime)