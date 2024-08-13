# https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()
        for no in nums:
            q.put(no)
        cnt = len(nums)-k
        while cnt >= 0:
            max_no = q.get()
            cnt -= 1
        return max_no
        
