from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        level = 0
        # sub = []
        res = []
        self.helper(root,level,res)
        return res[::-1]
    
    def helper(self,root,level,res):
        if not root:
            return 
        if len(res)==level:
            res.append([])
        if root.left:
            self.helper(root.left,level+1,res)
        if root.right:
            self.helper(root.right,level+1,res)
        res[level].append(root.val)
        