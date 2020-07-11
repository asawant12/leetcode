# https://leetcode.com/problems/decompress-run-length-encoded-list/
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        if len(nums) < 2:
            return output
        index=0
        while index < len(nums):
            freq = nums[index]
            val = nums[index+1]
            output.extend([val for i in range(freq)])
            index += 2
        return output
