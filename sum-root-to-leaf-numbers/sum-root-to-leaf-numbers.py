# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        num = root.val
        val=0
        self.helper(root,val,res)
      
        return sum(res)
    
    def helper(self,root,val,res):
        if not root:
            return 
        if not root.left and not root.right:
            val=val*10+root.val
            res.append(val)
            return 
        if root:
            val=val*10+root.val
          
        self.helper(root.left,val,res)
           
        self.helper(root.right,val,res)
            

            