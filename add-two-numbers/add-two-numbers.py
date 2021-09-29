# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        current = dummy
        carry =0
        val=0
        while l1 or l2:
            if l1:
                val+=l1.val
                l1=l1.next
            if l2:
                val+=l2.val
                l2=l2.next
            val+=carry 
     
            carry=val//10
            val = val%10
            node = ListNode(val)
            current.next=node
            current = current.next
            val=0
        if carry==1:
            current.next = ListNode(carry)
        return dummy.next     
            
                
            
         
                
            
            
        