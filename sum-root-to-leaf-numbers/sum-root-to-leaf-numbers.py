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
        exp = 0
        self.helper(root,num,exp+1,res)
        print(res)
        return sum(res)
    
    def helper(self,root,num,exp,res):
        if not root.left and not root.right:
            # num = num*10**exp+root.val 
            res.append(num)
            return 
        if root.left:
            
            self.helper(root.left,num*10+root.left.val ,exp+1,res)
        if root.right:
            # num = num*(10**exp)+root.right.val 
            self.helper(root.right,num*10+root.right.val,exp+1,res)
            
            
            