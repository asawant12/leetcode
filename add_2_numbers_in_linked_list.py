# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        trav1 = l1
        trav2 = l2
        start = None
        carry_over = 0
        while trav1 is not None or trav2 is not None:
            val1 = trav1.val if trav1 is not None else 0
            val2 = trav2.val if trav2 is not None else 0
            total = val1 + val2 + carry_over
            carry_over = 0
            if total > 9:
                carry_over = int(total/10)
                total = total % 10
            l3 = ListNode()
            l3.val = total
            if start is None:
                start = l3
                trav3 = start
            else:
                trav3.next = l3
                trav3 = l3
            if trav1 is not None:
                trav1 = trav1.next
            if trav2 is not None:
                trav2 = trav2.next
        if carry_over != 0:
            l3 = ListNode()
            l3.val = carry_over
            trav3.next = l3
        return start
