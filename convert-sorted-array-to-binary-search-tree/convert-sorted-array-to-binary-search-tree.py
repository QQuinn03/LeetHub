# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums)
    
    def helper(self,nums):
        if not nums:
            return
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
     
        root = TreeNode(nums[mid])
  
        root.left = self.helper(nums[:mid])
        root.right = self.helper(nums[mid+1:])
        return root