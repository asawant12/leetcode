# https://leetcode.com/problems/next-permutation/
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 1
        peak = nums[0]
        peak_index = 0
        for index in range(len(nums)):
            if nums[index] > nums[index-1]:
                peak = nums[index]
                peak_index = index
        if peak_index == 0:
            nums.sort()
        else:
            swap_index = None
            if peak_index < len(nums)-1:
                if nums[peak_index-1] < nums[peak_index+1]:
                    swap_index = peak_index+1
            swap_peak_index = peak_index if swap_index is None else swap_index
                
            temp = nums[swap_peak_index]
            nums[swap_peak_index] = nums[peak_index-1]
            nums[peak_index-1] = temp
            if peak_index < len(nums)-1:
                pk_index = peak_index+1 if swap_index is None else peak_index
                nums_need_to_sort = nums[pk_index:]
                nums_need_to_sort.sort()
                nums = nums[:pk_index]
                nums.extend(nums_need_to_sort)
                
                
                
                
            
            
        
