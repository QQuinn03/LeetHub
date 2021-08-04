# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2:
            if not l1:
                dummy.next = l2
                l2 = l2.next 
            elif not l2:
                dummy.next = l1
                l1 = l1.next 
            elif l1.val <l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next 
            dummy = dummy.next    
        return cur.next         
                