# https://leetcode.com/problems/subsets/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        stack = []

        def dfs(index):
            if index >= len(nums):
                ans.append(stack.copy())
                return

            stack.append(nums[index])
            dfs(index+1)
            stack.pop()
            dfs(index+1)

        dfs(0)
        return ans
        
