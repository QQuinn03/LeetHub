# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        h1=list1
        h2=list2
        cur = dummy
        while h1 or h2:
            if not h2:
                cur.next = h1
                h1=h1.next 
                
            elif not h1:
                cur.next = h2
                h2=h2.next 
           
            elif h1.val>h2.val:
                cur.next = h2
                h2=h2.next 
            else:
                cur.next = h1
                h1=h1.next
            cur=cur.next 
        return dummy.next    
                
                