# from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        que=[root]
        res=[]
        while que:
            node=que.pop()
            res.append(node.val)
            if node.right:
                que.append(node.right)
            if node.left:
                que.append(node.left)
        return res        
        
       