# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root)
        return self.ans
    
    def helper(self,root):
        if not root:
            return 0
        l=self.helper(root.left)
        r=self.helper(root.right)
        self.ans += abs(l)+abs(r)
        return root.val+l+r-1
        