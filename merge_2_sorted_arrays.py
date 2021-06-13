
# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        for num in nums2:
            while num > nums1[index] and nums1[index] != 0:
                index += 1
            nums1.insert(index, num)
        if 0 in nums1:
            nums1 = nums1[:nums1.index(0)]
            print(nums1)
