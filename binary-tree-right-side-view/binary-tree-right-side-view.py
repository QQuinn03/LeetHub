from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        que = deque([root])
        next_level = []
        res = []
        
        while que:
            next_level = que
            que = deque([])
            
            while next_level:
                node = next_level.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(node.val)
        return res      
            