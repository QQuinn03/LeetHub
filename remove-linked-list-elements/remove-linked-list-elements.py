# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        
        
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        pre = dummy
        while cur:
            if cur.val!=val:
                
                pre = pre.next 
            else:
                pre.next = cur.next
            cur = cur.next 
            
        return dummy.next      