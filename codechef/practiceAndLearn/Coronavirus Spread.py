for _ in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    dist = []
    count = 1
    for i in range(1,n):
        if p[i]-p[i-1] <= 2:
            count = count + 1
        else:
            dist.append(count)
            count = 1
    dist.append(count)
    print(min(dist),max(dist))
