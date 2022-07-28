n = int(input())

for j in range(n):
    print(" "*(n-j-1),end="")
    for k in range(j+1):
        print("* ",end="")
    print()

for j in range(n-1):
    print(" "*(j+1),end="")
    print("* "*(n-j-1))