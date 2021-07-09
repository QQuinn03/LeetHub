# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.helper(1,n)
      
    def helper(self,start,end):
        if start>end:
            return [None]
        res = []
        for i in range(start,end+1):
            l = self.helper(start,i-1)
            r = self.helper(i+1,end)
            for l_ in l:
                for r_ in r:
                    root = TreeNode(i)
                    root.left = l_
                    root.right = r_
                    res.append(root)
        return res     
        
        
