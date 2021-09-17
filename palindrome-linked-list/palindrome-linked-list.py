# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        pre = None
        slow = head
        fast = head
        
        while fast and fast.next:
            # pre = head
            slow = slow.next 
            fast = fast.next.next 
        mid = slow
        pre = None
        
        while mid:
            nxt = mid.next 
            mid.next = pre
            pre=mid 
            mid = nxt
        while pre and head:
            if pre.val!=head.val:
                return False
            pre = pre.next 
            head=head.next 
        return True     
            
            