l =  list(map(int,input().split()))

l.sort()
p1 = l[-1] * l[-2] *l [-3]
p2 = l[0] * l[1] *l[-1]

print(max(p1,p2))


'''

38 84 -99 -105 -37 218 166
3039792

'''