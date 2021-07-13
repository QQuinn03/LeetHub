# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        path = []
        self.helper(root,targetSum,res,path)
        return res
    
    def helper(self,root,target,res,path):
         
        if root and not root.left and not root.right and root.val ==target:
            path.append(root.val)
            res.append(path)
            return 
        if not root:
            return 
   
        target-=root.val
        self.helper(root.left,target,res,path+[root.val])
        self.helper(root.right,target,res,path+[root.val])
        