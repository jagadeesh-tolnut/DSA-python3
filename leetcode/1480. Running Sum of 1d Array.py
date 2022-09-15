class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumarr = []
        s = 0
        for i in nums:
            s += i
            sumarr.append(s)
        return sumarr
