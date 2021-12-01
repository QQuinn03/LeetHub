import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        que = []
        for i in lists:
            if i:
                heapq.heappush(que,(i.val,i))
      
        dummy = ListNode(0)
        cur=dummy
        while que:
            lval,l=heapq.heappop(que)
            
            cur.next = ListNode(lval)
            cur=cur.next
            if l.next:
                l=l.next 
                heapq.heappush(que,(l.val,l))
        return dummy.next         
                
            
        