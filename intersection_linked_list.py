#https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        travA=headA
        travB=headB
        while travA != travB:
            travA = headB if travA == None else travA.next
            travB = headA if travB == None else travB.next
        return travA
