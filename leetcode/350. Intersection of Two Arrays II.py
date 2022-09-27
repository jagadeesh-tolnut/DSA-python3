class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []
        for i in nums2:
            if i in nums1:
                temp.append(i)
                nums1.remove(i)
        return temp