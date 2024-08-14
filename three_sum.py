# https://leetcode.com/problems/3sum/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return 
        nums = sorted(nums)
        op = set()
        base_ptr = 0
        left = 1
        right = len(nums)-1
        while base_ptr <= len(nums)-3:
            while right > left:
                three_sum = nums[base_ptr] + nums[left] + nums[right]
                if three_sum == 0:
                    op.add((nums[base_ptr],nums[left],nums[right]))
                if three_sum > 0:
                    right -= 1
                else:
                    left += 1
            base_ptr += 1
            left = base_ptr + 1
            right = len(nums)-1
        return op
