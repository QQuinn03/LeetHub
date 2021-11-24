# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root,p,q)
    
    def helper(self,root,p,q):
        if not root:
            return 
        if root.val ==p.val:
            return p
        if root.val==q.val:
            return q
        l=self.helper(root.left,p,q)
        r=self.helper(root.right,p,q)
        
        if l and r:
            return root
        if l or r:
            return l or r
        
       
        
 
        