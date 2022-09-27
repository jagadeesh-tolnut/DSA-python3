class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        matr = len(mat)
        matc = len(mat[0])
        if matr*matc != r*c:
            return mat
        reshape = []
        temp = []
        t_c = c
        for i in mat:
            for j in i:
                temp.append(j)
                t_c -= 1
                if t_c == 0:
                    reshape.append(temp)
                    temp = []
                    t_c = c
        return reshape