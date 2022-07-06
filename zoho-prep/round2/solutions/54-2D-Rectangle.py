row = int(input())
mat = []

for i in range(row):
    mat.append(list(map(int,input().split())))

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())

for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        print(mat[i][j],end=" ")
    print()
