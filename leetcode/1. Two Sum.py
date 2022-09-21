class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in hp:
                return [hp[dif], i]
            hp[n] = i
