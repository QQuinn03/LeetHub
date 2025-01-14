from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        res=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root = root.left 
            else:
                node=stack.pop()
                res.append(node.val)
              
                root=node.right
        return res        