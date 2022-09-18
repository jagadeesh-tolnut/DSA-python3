class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1], [1, 1]]
        prev = [1, 1]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return output
        else:
            for _ in range(numRows - 2):
                temp = []
                temp.append(1)
                for i in range(len(prev) - 1):
                    temp.append(prev[i] + prev[i + 1])
                temp.append(1)
                output.append(temp)
                prev = temp.copy()

        return output