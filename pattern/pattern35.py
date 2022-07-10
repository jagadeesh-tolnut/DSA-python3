n = int(input())

for _ in range(n):
    for i in range(_+1):
        print(i+1,end="")

    print(" "*(2*n-2*(_+1)),end="")

    for i in range(_+1):

        print(_-i+1,end="")
    print()


"""

4
1      1
12    21
123  321
12344321

"""