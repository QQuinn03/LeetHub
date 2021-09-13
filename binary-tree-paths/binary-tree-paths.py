# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        self.helper(root,res,"")
        return res
    
    def helper(self,root,res,path):
        if root:
            if not root.left and not root.right:
                
                res.append(path+str(root.val))
                return 
            else:
                self.helper(root.right,res,path+str(root.val)+"->")
            
                self.helper(root.left,res,path+str(root.val)+"->")
        else:
            return 
                