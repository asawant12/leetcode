# https://leetcode.com/problems/sort-colors/description/

import heapq
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return []
        heap = []
        while len(nums):
            num = nums.pop()
            heapq.heappush(heap, num)

        while len(heap) > 0:
            nums.append(heapq.heappop(heap))
        return nums 
