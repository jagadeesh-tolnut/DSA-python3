n = int(input())
alpha = ord("A")
for i in range(1,n+1):
    for j in range(i):
        print(chr(alpha+n-i+j),end=" ")
    print()

