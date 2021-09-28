from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        left = True
        que=deque([root,None])
        level = deque([])
        res=[]
        while que:
            root = que.popleft()
            if root:
                if left:
                    level.append(root.val)
                else:
                    level.appendleft(root.val)
                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)
            else:
                left = not left
                res.append(level)
                level = deque([])
                if len(que)>0:
                    que.append(None)
        return res        
                
                
                
        