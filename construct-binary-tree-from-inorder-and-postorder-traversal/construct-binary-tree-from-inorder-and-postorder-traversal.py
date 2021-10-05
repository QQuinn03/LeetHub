# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder)==0:
            return 
        if len(postorder)==1:
            return TreeNode(postorder.pop())
        
        val = postorder[-1]
        idx = inorder.index(postorder.pop())
        root = TreeNode(val)
        
        root.right = self.buildTree(inorder[idx+1:],postorder)
        root.left = self.buildTree(inorder[:idx],postorder)
        
        
        return root