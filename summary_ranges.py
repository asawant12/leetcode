# https://leetcode.com/problems/summary-ranges/
class Solution:
    def get_range(self, range_of_nums):
        op=""
        if len(range_of_nums) > 1:
            op = f"{range_of_nums[0]}->{range_of_nums[-1]}"
        else:
            op = f"{range_of_nums[0]}"
        return op
        
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        cntr = None
        range_of_nums = []
        for num in nums:
            if cntr is None or num == cntr+1:
                range_of_nums.append(num)
                cntr = num
            else:
                output.append(self.get_range(range_of_nums))    
                cntr = num
                range_of_nums = [cntr]
        if len(range_of_nums)>0:
            output.append(self.get_range(range_of_nums))
        return output
                    
                
        
