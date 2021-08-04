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
        heap = []
        for l in lists:
            if l:
                heappush(heap,[l.val,l])
        
        dummy = ListNode(0)
        cur = dummy
        while heap:
            val,l = heappop(heap)
            node = ListNode(val)
            cur.next = node
            cur = cur.next 
            if l.next:
                l = l.next 
                heappush(heap,[l.val,l])
        return dummy.next          
            
                