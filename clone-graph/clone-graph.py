from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        que=deque([node])
        visited={}
        visited[node]=Node(node.val,[])
        
        while que:
            n = que.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    visited[nei]=Node(nei.val,[])
                    que.append(nei)
                visited[n].neighbors.append(visited[nei])
        
        return visited[node]          
              