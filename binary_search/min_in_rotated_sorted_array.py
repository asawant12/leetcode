# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0 , len(nums)-1
        ans = float("inf")
        while left < right:
            mid = (left + right) // 2
            ans = min(ans, nums[mid])

            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return min(ans, nums[left])
