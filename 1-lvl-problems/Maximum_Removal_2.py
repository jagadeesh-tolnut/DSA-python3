def is_allsame(l):
    if len(set(l)) == 1:
        return True
    else:
        False

N, S = map(int,input().split())
C = list(map(int,input().split()))

low = min(C)
got_back = 0

while (got_back < S or sum(C)<0):
    if is_allsame(C):
        C[0] -= 1
        low -= 1

    for i in range(N):
        if C[i] > low:
            temp = C[i]-low
            got_back += temp
            C[i] -= temp


if sum(C)<0:
    print(-1)
else:
    print(min(C))
