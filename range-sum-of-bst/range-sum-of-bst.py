# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if L<=root.val<=R:
            self.total+=root.val 
        self.rangeSumBST(root.left,L,R)
        self.rangeSumBST(root.right,L,R)
        return self.total
       