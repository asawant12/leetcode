
#https://leetcode.com/problems/shuffle-an-array/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-three-months
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums_initial = nums
        self.nums = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.nums_initial.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# nums = [1,2,3]
# obj = Solution(nums)
# param_2 = obj.shuffle()
# param_1 = obj.reset()
# param_2 = obj.shuffle()
