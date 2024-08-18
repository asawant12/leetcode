# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left = left + 1
                nums[left] = nums[right]
                right += 1
        left = left + 1
        return left 
