st = input()
l = len(st)
half = l//2
for i in range(half):
    print(" "*i,end="")
    print(st[i],end="")
    print(" "*(l-(2*i)-2),end="")
    print(st[l-i-1])

print(" "*half,end="")
print(st[half])

for i in range(half-1,-1,-1):
    print(" " * i, end="")
    print(st[i], end="")
    print(" " * (l - (2 * i)-2), end="")
    print(st[l - i-1])