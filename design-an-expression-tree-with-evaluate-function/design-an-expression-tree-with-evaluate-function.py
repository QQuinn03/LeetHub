import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    # define your fields here

    def evaluate(self) -> int:
        pass
    
class TreeNode():

    def __init__(self, val, op=None):
        self.left = None
        self.right = None
        self.op = op
        self.val = val
        
    def evaluate(self):
        if self.op==None:
            return int(self.val)
        
        if self.op == "+":
            return self.left.evaluate() + self.right.evaluate()
        if self.op == "-":
            return self.left.evaluate() - self.right.evaluate()
        if self.op == "*":
            return self.left.evaluate() * self.right.evaluate()
        if self.op == "/":
            return self.left.evaluate() // self.right.evaluate()
    
        
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""     


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack=[]
        op=set(['-','+','*','/']) 
        
        for i in postfix:
           
            if i not in op:
           
                node=TreeNode(i)
                stack.append(node)
                
            else:
        
                node=TreeNode(0,i)
         
                node1=stack.pop()
                node2=stack.pop()
                node.right=node1
                node.left=node2
                
                stack.append(node)
               
        return stack[-1]        
                
    
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        