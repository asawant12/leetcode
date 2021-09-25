# Facbook interview: https://leetcode.com/problems/top-k-frequent-elements/

from queue import PriorityQueue
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = []
        count = Counter(nums)
        q = PriorityQueue(maxsize=k)
        for (num, freq) in count.items():
            if not q.full():
                q.put((freq, num))
            else:
                latest_freq, latest_num = q.get()
                if freq > latest_freq:
                    q.put((freq, num))
                else:
                    q.put((latest_freq, latest_num))
        while not q.empty():
            freq, num = q.get()
            topk.insert(0, num)
        return topk
