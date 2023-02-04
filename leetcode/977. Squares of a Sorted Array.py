class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sa = []
        for n in nums:
            sa.append(n*n)
        sa.sort()

        return sa