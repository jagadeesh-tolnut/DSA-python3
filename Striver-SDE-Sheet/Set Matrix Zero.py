import copy


row = int(input())
mat = []

for i in range(row):
    temp_row = list(map(int,input().split()))
    mat.append(temp_row)

col = len(mat[0])

new_mat = copy.deepcopy(mat)
for i in range(row):
    for j in range(col):
        if mat[i][j] == 0:

            for n in range(row):
                new_mat[n][j] = 0
            
            for m in range(col):
                new_mat[i][m] = 0
            
for r in new_mat:
    print(*r)



'''

i/p
3
0 1 2 0
3 4 5 2
1 3 1 5

o/p:
0 0 0 0
0 4 5 0
0 3 1 0


'''