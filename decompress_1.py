# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        index=0
        total = len(nums)
        decomperss = []
        while index < total-1:
            freq = nums[index]
            val = nums[index+1]
            decomp_list = [val]*freq
            decomperss.extend(decomp_list)
            index += 2
        return decomperss
            
