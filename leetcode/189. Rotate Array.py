class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k < 0:
            for i in range(k):
                nums.append(nums.pop(0))
        elif k > 0:
            for i in range(k):
                nums.insert(0,nums.pop())