n = int(input())
print(" "*(n-1)+"*")

f_space = n-2
mid_space = 1

for i in range(n-1):
    if mid_space<=n:
        print(" "*f_space+"*"+" "*mid_space+"*")
        f_space -= 1
        mid_space += 2
    else:
        print("*"*(n*2-1))
        



'''

5
    *
   * *
  *   *
 *     *
*********


'''