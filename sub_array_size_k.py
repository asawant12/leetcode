# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = k-1
        no_of_lists = 0
        while right < len(arr):
            avg = int(sum(arr[left:right+1])/k)
            if avg >= threshold:
                no_of_lists += 1
            left += 1
            right += 1
        return no_of_lists
            
        
