# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        
        list_freq = [ (cnt, num) for num, cnt in frequency.items()]
        list_freq.sort()
        ans = []
        while k > 0:
            freq, item = list_freq.pop()
            ans.append(item) 
            k -= 1
        return ans


        
