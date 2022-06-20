n = int(input())
reached_mid = False
star = n
space = 0

for i in range(n*2):
    if reached_mid:
        print(" "*space + "* "*star)
        space -= 1
        star += 1
    else:
        print(" "*space + "* "*star)  
        space += 1
        star -= 1

    if star == 0:
        reached_mid = True
        star += 1
        space -= 1
        # print(" "*space + "* "*star)


'''

5
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

'''


