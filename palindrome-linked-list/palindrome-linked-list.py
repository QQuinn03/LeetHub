# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pre=ListNode(0)
        pre.next =head
        cur=head
        slow=head
        fast=head
        pre.next = cur
        
        while fast and fast.next:
            pre=pre.next
            slow=slow.next 
            fast=fast.next.next 
        if pre:
            pre.next =None
        
        second=None
        while slow:
            nxt=slow.next 
            slow.next = second
            second=slow
            slow=nxt
        while cur and second:
            if cur.val!=second.val:
                return False
            cur=cur.next
            second = second.next 
        return True    
        
        