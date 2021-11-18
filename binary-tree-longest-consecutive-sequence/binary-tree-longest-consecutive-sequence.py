# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max=0
        temp=1
        self.helper(root,None,temp)
        return self.max
      
    
    def helper(self,root,parent,temp):
        if not root:
            return 
        if parent!=None and parent.val==root.val-1:
            temp+=1
        else:
            temp=1
        self.max=max(self.max,temp)
        self.helper(root.left,root,temp)
        self.helper(root.right,root,temp)
            
            
      