# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = l1=ListNode(0)
        bigger = l2=ListNode(0)
        cur=head
        # less.next=cur 
        # # bigger.next=cur
        
        while cur:
            if cur.val<x:
                l1.next = cur
                l1=l1.next 
            else:
                l2.next = cur
                l2=l2.next 
            cur=cur.next
        l2.next = None   
        l1.next = bigger.next
        return less.next