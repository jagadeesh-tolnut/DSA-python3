n = int(input())
space = 0
star = n
n = n//2 + 1
for i in range(n):
    print(" "*space+"*"*star+" "*space)
    star -= 2
    space += 1



'''

9
*********
 ******* 
  *****  
   ***   
    *    

'''