row = int(input())
mat = []
for i in range(row):
    mat.append(list(map(int,input().split())))

col_end = len(mat[0])
row_end = row
r = 0
c = 0

while(row_end>r and col_end>c):
    for i in range(c,col_end):
        print(mat[r][i],end="->")
    r += 1

    for i in range(r,row_end):
        print(mat[i][col_end-1],end="->")
    col_end -= 1

    for i in range(col_end-1,c-1,-1):
        print(mat[row_end-1][i],end="->")
    row_end -= 1

    for i in range(row_end-1,r-1,-1):
        print(mat[i][c],end="->")
    c += 1

