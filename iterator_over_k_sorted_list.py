# https://leetcode.com/problems/merge-k-sorted-lists/
# Approach I - Using min heap
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        fin = []
        h = []
        for lst in lists:
            trav = lst
            while trav is not None:
                heapq.heappush(h, trav.val)
                trav = trav.next
        start = ListNode(-1)
        trav = start
        for i in range(len(h)):
            item = heapq.heappop(h)
            node = ListNode(item)
            trav.next = node
            trav = trav.next
        return start.next
      
      
# Approch -II Dvide and concur

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        fin = []
        h = []
        if lists is None or len(lists) == 0:
            return None
        return self.mergeLists(lists, 0, len(lists)-1)
    
    def mergeLists(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = (start - end)/2
        left = self.mergeLists(lists, start, mid)
        right = self.mergeLists(lists, mid+1, end)
        return self.merge(left, right)
    
    def merge(left, right):
        start = ListNode(-1)
        trav = start
        while (left is not None or right is not None):
            if left is None:
                trav.next = right
                right = right.next
            elif right is None:
                trav.next = left
                left = left.next
            elif left.val < right.val:
                trav.next = left
                left = left.next
            else:
                trav.next = right
                right = right.next
            trav = trav.next
        return start.next
        
