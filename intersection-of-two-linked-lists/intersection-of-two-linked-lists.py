# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hash_set = set()
        b_ = headB
        while b_:
            hash_set.add(b_)
            b_=b_.next 
        while headA:
            if headA in hash_set:
                return headA
            headA = headA.next 
        return None    
        