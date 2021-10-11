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
        self.pre = None
        self.head = None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        self.helper(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head
    
    def helper(self,root):
        if not root:
            return root
        self.helper(root.left)
        
        if self.pre:
            
            root.left = self.pre
            self.pre.right = root
        else:
            self.head = root
        self.pre = root
        
        self.helper(root.right)
        
        return root
            
        