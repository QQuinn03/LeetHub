# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n ==0:
            return []
   
        return self.helper(1,n)
    def helper(self,start,end):
        if start >end:
            return[None]
        res = []
        
        for i in range(start,end+1):
            all_left = self.helper(start,i-1)
            all_right = self.helper(i+1,end)
            
            for l in all_left:
                for r in all_right:
                    root_ = TreeNode(i)
                    root_.left = l
                    root_.right = r
                    res.append(root_)
        return res              
                    
        
