n = int(input())
a = ord("A")

for _ in range(n):
    for i in range(n - _):
        print(chr(a+n-_-i-1),end=" ")
    print()