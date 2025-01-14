# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1=dummy
        p2=dummy
        
        count = 0
        while count!=n:
            p1=p1.next 
            count+=1
        while p1.next!=None:
            p2=p2.next 
            p1=p1.next 
        p2.next =p2.next.next 
        return dummy.next 