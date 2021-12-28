# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res=self.dfs(root,p,q)
        res1=self.dfs(root,p,p)
        res2=self.dfs(root,q,q)
        
        if res and res1 and res2:
            return res
        return None
        
    def dfs(self,root,p,q):
        if not root:
            return None
        if root.val==p.val:
            return p
        if root.val ==q.val:
            return q
        
        l=self.dfs(root.left,p,q)
        r=self.dfs(root.right,p,q)
        
        if not l:
            return r
        if not r:
            return l 
     
        return root
        
        