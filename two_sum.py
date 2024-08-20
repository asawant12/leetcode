# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for (ind, val) in enumerate(nums):
            diff = target - val
            if diff not in mapping:
                mapping[val] = ind
            else:
                return [ind, mapping[diff]]            
