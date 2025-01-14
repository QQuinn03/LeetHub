# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder)==0:
            return 
        if len(preorder)==1:
            return TreeNode(preorder.pop(0))
        
        val = preorder[0]
        index = inorder.index(preorder.pop(0))
        root = TreeNode(val)
        
        root.left = self.buildTree(preorder,inorder[:index])
        root.right = self.buildTree(preorder,inorder[index+1:])
        return root