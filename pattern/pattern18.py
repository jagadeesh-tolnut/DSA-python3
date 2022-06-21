n = int(input())

for i in range(n):
    for j in range(n-i):
        print("*",end="")
    for k in range(2*i):
        print(" ",end="")
    for l in range(n-i):
        print("*",end="")
    print()

for i in range(n,0,-1):
    for j in range(n-i+1):
        print("*",end="")
    for k in range(2*i-2):
        print(" ",end="")
    for l in range(n-i+1):
        print("*",end="")
    print()

'''

5
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********


'''