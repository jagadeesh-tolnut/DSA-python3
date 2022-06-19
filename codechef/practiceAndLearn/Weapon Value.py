# cook your dish here
for _ in range(int(input())):
    n = int(input())
    fights = []
    for i in range(n):
        weapons = input()
        fights.append(weapons)
    
    alive_weapon = 0
    for j in range(0,10):
        temp = 0
        for i in fights:
            if i[j] == "1":
                temp += 1
        
        if temp%2==1:
            alive_weapon += 1
    
    print(alive_weapon)
