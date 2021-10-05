# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        
        mid = self.helper(head)
        node = TreeNode(mid.val)
        if mid ==head:
            return node
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
        
    def helper(self,head):
        # if not head:
        #     return 
        slow=head
        fast=head
        pre = head
        
        while fast and fast.next:
            pre = slow
            slow=slow.next 
            fast = fast.next.next
            
        if pre:
            pre.next = None
       
        return slow