# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res=0
        temp=0
        self.helper(root,None,temp)
        return self.res
    
    def helper(self,root,parent,temp):
        if not root:
            return 
        if parent!=None and root.val==parent.val+1:
            print(root.val,parent.val,temp)
            temp+=1
            
        else:
            temp=1
       
        self.res=max(self.res,temp)
        self.helper(root.left,root,temp)
        self.helper(root.right,root,temp)
            