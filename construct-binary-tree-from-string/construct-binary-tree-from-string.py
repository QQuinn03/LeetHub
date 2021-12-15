# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        
        stack=[]
        flag=1
        temp=""
        for i in s:
            if i=="-" or i.isdigit():
                temp+=i
                
            elif i=="(":
                if temp:
                  
                    node=TreeNode(int(temp))
                    stack.append(node)
                    temp=""
           
            elif i==")":
                if temp:
                    node=TreeNode(int(temp))
                    temp=""
                    if stack[-1].left==None:
                        stack[-1].left=node
                    else:
                        stack[-1].right=node
                else:
                    node=stack.pop()
                    if stack[-1].left==None:
                        stack[-1].left=node
                    else:
                        stack[-1].right=node
        if not s:
            return None
        if stack:
            return stack[-1]
        else:
            return TreeNode(int(s)) 
                        

         
                