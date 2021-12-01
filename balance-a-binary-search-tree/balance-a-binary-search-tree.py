# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        self.inorder(root,arr)
        return self.rebalance(arr)
    
    def rebalance(self,arr):
        if not arr:
            return 
        mid = len(arr)//2
        root=TreeNode(arr[mid])
        root.left = self.rebalance(arr[:mid])
        root.right = self.rebalance(arr[mid+1:])
        return root
        
    
    def inorder(self,root,arr):
        if not root:
            return 
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
        