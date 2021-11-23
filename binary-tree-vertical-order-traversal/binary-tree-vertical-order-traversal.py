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
            return []
        dic = defaultdict(list)
        que=deque([(root,0)])
        while que:
            node,level=que.popleft()
            dic[level].append(node.val)
            if node.left:
                que.append((node.left,level-1))
            if node.right:
                que.append((node.right,level+1))
        res=[]
        keys=sorted(dic.keys())
        for key in keys:
            res.append(dic[key])
        return res    
             