# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total = 0
        counter = 0
        while counter < k:
            max_element =  max(nums)
            total += max_element
            nums.remove(max_element)
            nums.append(max_element+1)
            counter += 1
        return total
