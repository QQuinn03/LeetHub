"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.dic = {}
    
    def helper(self,node):
        if node:
            if node in self.dic:
                return self.dic[node]
            else:
                new = Node(node.val)
                self.dic[node]=new
                return self.dic[node]
        return None    
            
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        current = self.helper(head)
        dummy = head
        while dummy:
            current.next = self.helper(dummy.next)
            current.random = self.helper(dummy.random)
            current = current.next 
            dummy  = dummy.next 
        return self.dic[head]    
        
        