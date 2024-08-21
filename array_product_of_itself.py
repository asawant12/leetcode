# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]* len(nums)
        prefix=1
        postfix=1
        for indx in range(len(nums)):
            ans[indx] = prefix
            prefix = prefix * nums[indx]
        for indx in range(len(nums)-1, -1, -1):
            ans[indx] = ans[indx] * postfix
            postfix *= nums[indx]
        return ans
