"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen=set()
        while p:
            if p in seen:
                return p
            seen.add(p)
            p=p.parent
        
        while q:
            if q in seen:
                return q
            seen.add(q)
            q=q.parent