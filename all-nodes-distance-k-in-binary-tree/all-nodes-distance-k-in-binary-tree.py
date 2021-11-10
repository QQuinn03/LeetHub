from collections import defaultdict,deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildGraph(self,node,parent,graph):
        if not node:
            return 
        if parent:
            graph[node].add(parent)
        if node.left:
            graph[node].add(node.left)
        if node.right:
            graph[node].add(node.right)
        self.buildGraph(node.left,node,graph)
        self.buildGraph(node.right,node,graph)
        return graph
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(set)
        graph = self.buildGraph(root,None,graph)
        
        que=deque([(target,0)])
        res=[]
        visited=set()
        while que:
            node,step=que.popleft()
            if step==K:
                res.append(node.val)
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    que.append((nei,step+1))
        return res            
                
        
                   