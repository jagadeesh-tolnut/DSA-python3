class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1, 1]
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return prev
        else:
            for _ in range(rowIndex - 1):
                temp = []
                temp.append(1)
                for i in range(len(prev) - 1):
                    temp.append(prev[i] + prev[i + 1])
                temp.append(1)
                prev = temp.copy()

        return prev