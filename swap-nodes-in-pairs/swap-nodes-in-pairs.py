# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head 
        
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy 
        
        while cur.next and cur.next.next:
            temp = cur.next
            cur.next =cur.next.next 
            temp.next = temp.next.next 
            cur.next.next=temp 
            cur = cur.next.next 
        return dummy.next      