class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        r = sum(nums) - nums[0]
        l = 0
        for i in range(n-1):
            if l == r:
                return i
            else:
                l += nums[i]
                r -= nums[i+1]
        if sum(nums[:n-1]) == 0:
            return n-1
        return -1