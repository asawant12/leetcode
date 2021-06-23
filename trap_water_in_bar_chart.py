# https://leetcode.com/problems/trapping-rain-water/solution/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        water=0
        block = 0
        max_lefts = []
        max_rts = []
        lft_max = rt_max = 0
        for block in height:
            max_lefts.append(lft_max)
            lft_max = max(lft_max, block)

        index = len(height)-1
        while index >= 0:
            max_rts.insert(0, rt_max)
            rt_max = max(rt_max, height[index])
            index -= 1
        
        print(max_lefts)
        print(max_rts)
        while block < len(height)-1:
            water_level = min(max_lefts[block], max_rts[block])
            curr_water = water_level - height[block]
            water = water + curr_water
        return water
        
