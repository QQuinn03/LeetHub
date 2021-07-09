from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        is_left = True
        que = deque([root,None])
        res = []
        level = deque([])
        while que:
            node = que.popleft()
            if node:
                if is_left:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            else:
                is_left = not is_left
                if len(que)>0:
                    que.append(None)
                res.append(level)
                level = deque([])
        return res
                    
                    
                
        