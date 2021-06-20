# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(-1)
        start.next = head
        slow_trav = start
        fast_trav = head
        counter = 0

        while fast_trav is not None and fast_trav.next is not None:
            fast_trav = fast_trav.next.next
            slow_trav = slow_trav.next
            counter += 1
        total_nodes = 2 * counter if fast_trav is None else (2 * counter) + 1
        
        dest = total_nodes - n + 1
        
        if dest <= counter:
            counter = 0
            trav = start
        else:
            trav = slow_trav
        while counter < dest - 1:
            trav = trav.next
            counter += 1
        temp = trav.next.next if trav.next.next is not None else None
        del trav.next
        trav.next = temp
        return start.next
