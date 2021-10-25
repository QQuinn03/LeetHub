# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        
        size = 0
        while cur:
            cur = cur.next 
            size+=1
        
        m = size-n
        fast = head
        slow = dummy
        while m!=0:
            slow = slow.next 
            #fast = fast.next 
            m-=1
        slow.next = slow.next.next 
        return dummy.next 
            
            
            
            
        