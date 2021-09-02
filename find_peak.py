# https://leetcode.com/problems/find-peak-element/

class Solution:
    
    def search(self, nums, left, right):
        if self.peak_index != 0:
            return
        mid = int((right -left)/2)
        mid = left + mid
        if mid != 0 and mid < (len(nums)-1):
            if nums[mid] > nums[mid-1 ] and nums[mid] > nums[mid+1]:
                self.peak_index = mid
                return
            else:
                self.search(nums, left, mid)
                self.search(nums, mid,right)
        
        
        
        
    def findPeakElement(self, nums: List[int]) -> int:
        self.peak_index = 0
        self.search(nums, 0, len(nums)-1)
        return self.peak_index
