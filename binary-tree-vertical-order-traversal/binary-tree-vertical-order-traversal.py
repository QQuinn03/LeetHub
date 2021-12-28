from collections import deque,defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root

        que=deque([(root,0)])
        max_level=float("-inf")
        min_level=float("inf")
        dic=defaultdict(list)
        while que:
            node,level=que.popleft()
            dic[level].append(node.val)
            if node:
                max_level=max(level,max_level)
                min_level=min(level,min_level) 
            if node.left:
                que.append((node.left,level-1))
            if node.right:
                que.append((node.right,level+1))
       
        res=[]
        for i in range(min_level,max_level+1):
            res.append(dic[i])
        return res    

             