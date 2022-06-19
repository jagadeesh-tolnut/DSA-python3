n = int(input())
maxn =  2*n - 1
reach_mid = False
star_no = 1

for i in range(maxn):
    if star_no == n:
        print("* "*star_no)
        reach_mid = True
        star_no -= 1
    elif reach_mid:
        print("* "*star_no)
        star_no -= 1
    else:
        print("* "*star_no)
        star_no += 1

    
        
