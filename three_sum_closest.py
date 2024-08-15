#https://leetcode.com/problems/3sum-closest/

import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        three_sum=sys.maxsize
        pivot=0
        left=1
        rt=len(nums)-1
        while pivot < len(nums)-2:
            while rt > left:
                total=nums[pivot] + nums[left] + nums[rt]
                if total > target:
                    rt -= 1
                else: # important conditon
                    left += 1
                if abs(total - target) < abs(three_sum - target):  # was stuck here <<<<< 
                    three_sum = total
            pivot += 1
            left = pivot + 1
            rt=len(nums)-1
        return three_sum

                
            
