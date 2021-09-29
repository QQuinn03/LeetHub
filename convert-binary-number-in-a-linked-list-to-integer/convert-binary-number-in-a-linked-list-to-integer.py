# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        arr=[]
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next 
        
        power=0
        res=0
        for i in range(len(arr)-1,-1,-1):
            res+=arr[i]*(2**power)
            power+=1
        return res    