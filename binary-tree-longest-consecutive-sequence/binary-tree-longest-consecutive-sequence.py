# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.size=0
        self.helper(root,None,0)
        return self.size 
    
    def helper(self,root,parent,length):
        if not root:
            return 
        if parent!=None and parent.val+1==root.val:
            length+=1
        else:
            length=1
        self.size=max(self.size,length)    
        self.helper(root.left,root,length)
        self.helper(root.right,root,length)
     