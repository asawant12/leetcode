# https://leetcode.com/problems/container-with-most-water/submissions/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        total_lines = len(height)
        area = 0
        left = 0
        right = total_lines-1
        while left < right:
            new_area = min(height[left], height[right]) * (right-left)
            area = max(area, new_area)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
            
        return area
