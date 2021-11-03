t = int(input())
for _ in range(t):
    n, x, p = map(int, input().split())
    neg = n-x
    if p<= (x*3)-neg:
        print("PASS")
    else:
        print("FAIL")