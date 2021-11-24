"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def __init__(self):
        self.tail=None
        self.head = None
        
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.helper(root)
        self.head.left = self.tail
        self.tail.right =self.head 
        return self.head  
    def helper(self,root):
        if not root:
            return None
        self.helper(root.left)
        
        if self.head:
            root.left=self.tail 
            self.tail.right = root
        if not self.head:
            self.head = root
        self.tail = root
        
        self.helper(root.right )
        return self.tail
        
        