n = int(input())
mid = n//2
star = 1
n = n//2 + 1
for i in range(n):
    print(" "*mid+"*"*star+" "*mid)
    mid -= 1
    star += 2


'''

9
    *    
   ***   
  *****  
 ******* 
*********

'''