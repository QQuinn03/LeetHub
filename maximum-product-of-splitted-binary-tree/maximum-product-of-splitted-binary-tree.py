# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        res=[]
        total_sum=self.dfs(root,res)
        max_val=float("-inf")
      
        for i in res:
            temp=i*(total_sum-i)
            if temp>max_val:
                max_val=temp
        return max_val% (10**9 + 7)
    
    def dfs(self,root,res):
        if not root:
            return 0
        
        l=self.dfs(root.left,res)
        r=self.dfs(root.right,res)
      
        res.append(root.val+l+r)
        return root.val+l+r
        