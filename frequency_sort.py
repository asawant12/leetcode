# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/?envType=daily-question&envId=2024-07-23
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        sortedArray = []
        freq_map = {}
        inv_freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq = nums.count(num)
                freq_map[num] = freq
        for (num, freq) in freq_map.items():
            if freq not in inv_freq_map:
                inv_freq_map[freq] = [num]
            else:
                inv_freq_map[freq].append(num)
        freqs = list(inv_freq_map.keys())
        freqs.sort()
        for freq in freqs:
            nums =  inv_freq_map[freq]
            nums.sort(reverse=True)
            for num in nums:
                sortedArray.extend([num]*freq)
        return sortedArray
        
