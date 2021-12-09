# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        pre=None
        while head:
            temp=head.next 
            head.next=pre
            pre=head
            head=temp
        
        return pre