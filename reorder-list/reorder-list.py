# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy= ListNode(0)
        dummy.next = head
        first = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
       
        second = slow.next
        slow.next = None
        
        pre = None
        while second:
            nxt = second.next 
            second.next = pre
            pre = second
            second = nxt
        insert = pre
 
        while insert:
            temp = first.next 
            first.next = insert
            first = temp
            temp = insert.next 
            insert.next = first
            insert = temp
            
        return dummy.next    
            
            