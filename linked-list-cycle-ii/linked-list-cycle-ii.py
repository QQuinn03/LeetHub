# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            if slow ==fast:
                break
        else:        
            return None
    
        print(slow.val,fast.val)
        cur = head
        while cur !=slow:
            cur = cur.next 
            slow = slow.next 
        print(cur.val)    
        return cur    