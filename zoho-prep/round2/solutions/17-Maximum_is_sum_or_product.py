def sum_of_int(num):
    n = num
    sum_of_digits = 0
    while n > 0:
        temp = n%10
        sum_of_digits += temp
        n = n // 10
    return sum_of_digits

def prod_of_int(num):
    n = num
    prod_of_digits = 1
    while n > 0:
        temp = n%10
        prod_of_digits *= temp
        n = n // 10
    return prod_of_digits

l = list(map(int,input().split()))

for i in l:
    print(max(sum_of_int(i),prod_of_int(i)),end=" ")


'''

120 24 71 10 59
3 8 8 1 45 

'''