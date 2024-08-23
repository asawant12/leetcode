# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        left_max=0
        rt_max=0
        total_trap = 0
        while left < right:
            left_max = max(left_max, height[left])
            rt_max = max(rt_max, height[right])
            if left_max < rt_max:
                trap = left_max - height[left]
                left +=1
            else:
                trap = rt_max - height[right]
                right -= 1
            if trap > 0:
                total_trap += trap
        return total_trap
