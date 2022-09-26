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
        val=0
        temp=0
        head = ListNode(0)
        temp=head
        carry=0
        while l1 or l2:
            if l1:
                val+=l1.val
                l1=l1.next
            if l2:
                val+=l2.val
                l2=l2.next
                
            val+=carry
            digit = val%10
            carry=val//10
            node = ListNode(digit)
            temp.next=node 
            temp=temp.next
            val=0
        if carry==1:
            node=ListNode(1)
            temp.next=node
    
        return head.next        
            
                