# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        self.helper(root,sum)
        self.pathSum(root.left,sum)
        self.pathSum(root.right,sum)
        
        return self.count
    def helper(self,root,target):
        if not root:
            return 0
        if root.val ==target:
       
            self.count+=1
   
        self.helper(root.left,target-root.val)
        self.helper(root.right,target-root.val)
        