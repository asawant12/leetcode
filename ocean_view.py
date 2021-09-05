# https://leetcode.com/problems/buildings-with-an-ocean-view/submissions/

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = heights[-1]
        length_height = len(heights)
        ocean_view = [length_height-1]
        index =  length_height - 2
        while index >= 0:
            if heights[index] > max_height:
                ocean_view.append(index)
                max_height = heights[index]
            index -= 1
        return sorted(ocean_view)
