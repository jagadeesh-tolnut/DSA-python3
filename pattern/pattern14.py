n = int(input())
mid_space = n
print("*"*(n*2-1))
f_space = 1
mid_spce = n

for i in range(n-1):
    if mid_space>=1:
        print(" "*f_space+"*"+" "*mid_space+"*")
        f_space += 1
        mid_space -= 2
    else:
        print(" "*f_space+"*")


'''

5
*********
 *     *
  *   *
   * *
    *


'''