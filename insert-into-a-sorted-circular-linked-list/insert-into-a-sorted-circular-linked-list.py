"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head==None:
            newNode=Node(insertVal,None)
            newNode.next=newNode
            return newNode
        pre=head
        cur=head.next 
        flag=False
        
        while True:
            if pre.val<=insertVal<=cur.val:
                flag=True
            elif pre.val>cur.val:
                if insertVal>=pre.val or insertVal<=cur.val:
                    flag=True
                    
            if flag:
                pre.next = Node(insertVal,cur)
                return head
            
            pre=cur
            cur=cur.next 
            
            if pre==head:
                break
                
        pre.next = Node(insertVal,cur)
        return head