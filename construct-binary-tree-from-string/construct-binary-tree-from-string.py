# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        stack=[]
        num=""
        for i in s:
            if i.isdigit() or i=="-":
                num +=i
            elif i=="(":
                if num:
                    node=TreeNode(int(num))
                    stack.append(node)
                    num=""
            else:
                if num:
                    node =TreeNode(int(num))
                    num=""
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
                    
                
                