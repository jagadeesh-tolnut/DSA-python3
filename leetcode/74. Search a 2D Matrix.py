class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pos = -1
        r = len(matrix)
        if matrix[0][0] > target:
            return False

        for i in range(r):
            if matrix[i][0] > target:
                pos = i - 1
                break
            pos = i

        for i in matrix[pos]:
            if i == target:
                return True
        return False