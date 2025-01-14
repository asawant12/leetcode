# https://leetcode.com/problems/paint-house/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-three-months

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0,0,0]
        for house in costs:
            dp0 = house[0] + min(dp[1], dp[2])
            dp1 = house[1] + min(dp[0], dp[2])
            dp2 = house[2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]
        return min(dp)
