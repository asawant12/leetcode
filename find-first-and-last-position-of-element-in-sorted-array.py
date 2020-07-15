# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        try:
            index = nums.index(target)
        except ValueError:
            return [-1, -1]
        while nums[index] == target:
            output.append(index)
            index += 1
            if index == len(nums):
                break
        if len(output)==1:
            output.append(output[0])
        fin_output = [output[0], output[-1]]
        return fin_output
