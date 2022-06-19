# cook your dish here
for _ in range(int(input())):
    n , orgin = map(str,input().split())
    n = int(n)
    laddu = 0
    for i in range(n):
        act = input().split()
        if act[0] == "CONTEST_WON":
            if int(act[1]) < 20:
                laddu = laddu + 300 + (20-int(act[1]))
            else:
                laddu = laddu + 300
        
        elif act[0] == "TOP_CONTRIBUTOR":
            laddu = laddu + 300
        
        elif act[0] == "BUG_FOUND":
            laddu = laddu + int(act[1])
        
        elif act[0] == "CONTEST_HOSTED":
            laddu = laddu + 50
        
        else:
            print("lusu")
            
    if orgin == "INDIAN":
        print(laddu//200)
    else:
        print(laddu//400)
