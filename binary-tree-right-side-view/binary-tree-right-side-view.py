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
            return[]
        res=[]
        que=deque([root])
        level=deque([])
        
        while que:
            level=que
            que=deque([])
            while level:
                node = level.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(node.val)
        return res     