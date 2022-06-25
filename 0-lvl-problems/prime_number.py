import sys

def is_prime(num):
    if num<2 and num > -1:
        return False
    
    for i in range(2,n):
        if num % i == 0:
            return False
    
    return True


n = int(input())
print(is_prime(n))
        
    
