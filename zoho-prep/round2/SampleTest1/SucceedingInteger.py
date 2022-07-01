n = list(map(str,input().split(",")))
st = ""

for i in n:
    st += i

inc_no = str(int(st)+1)
print(",".join(inc_no))