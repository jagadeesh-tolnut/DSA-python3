n = int(input())

reach_mid = False
print(" "*(n-1)+"*")
f_space = n-2
mid_space = 1

for i in range(n*2-3):
    if reach_mid:
        print(" "*f_space+"*"+" "*mid_space+"*")
        mid_space -= 2
        f_space += 1

    else:
        print(" "*f_space+"*"+" "*mid_space+"*")
        f_space -= 1
        mid_space += 2

    if f_space == 0:
        reach_mid = True

print(" "*(n-1)+"*")



'''

5
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *


'''