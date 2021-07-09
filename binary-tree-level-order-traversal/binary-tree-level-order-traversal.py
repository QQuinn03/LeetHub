from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        res = []
        level = 0
        
        while que:
            res.append([])
            size = len(que)
            for i in range(size):
                node = que.popleft()
                res[level].append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level+=1
        return res     
                
            