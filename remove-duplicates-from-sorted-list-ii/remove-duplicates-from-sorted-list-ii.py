# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        
        while cur and cur.next:
            if cur.val ==cur.next.val:
                while cur.next and cur.val ==cur.next.val:
                    cur = cur.next 
                    
                pre.next = cur.next
                cur = cur.next 
            else:
                pre = pre.next 
                cur = cur.next 
        return dummy.next          
        
        