t = int(input())
for _ in range(t):
    s = input()
    a=0
    b=0
    for i in s:
        if i=="a":
            a=a+1
        else:
            b=b+1
    print(min(a,b))