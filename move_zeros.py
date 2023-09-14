# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_ptr = 0
        secnd_ptr = 1
        while secnd_ptr < len(nums):
            if nums[first_ptr] == 0:
                temp = nums[first_ptr]
                nums[first_ptr] = nums[secnd_ptr]
                nums[secnd_ptr] = temp
            if nums[first_ptr] != 0:
                first_ptr += 1
            secnd_ptr += 1
        return nums
