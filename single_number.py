# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        elements = len(nums)
        count = 0
        scanned = []
        while count < elements:
            num = nums.pop()
            if (num not in nums and num not in scanned) or len(nums) == 0:
                return num
            scanned.append(num)
            count += 1
