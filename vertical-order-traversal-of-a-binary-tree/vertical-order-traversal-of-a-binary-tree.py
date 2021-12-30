# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return[]
        col =0
        row=0
        res=[]
        self.helper(root,res,col,row)
        res.sort()

        output=defaultdict(list)
        for i in res:
            col,row=i[0]
            val=i[1]
            output[col].append(val)
        
        arr=[]
        for key,val in output.items():
            arr.append(val)
        return arr    
      
            
     
    def helper(self,root,res,col,row):
        if not root:
            return []
        res.append(((col,row),root.val))
        self.helper(root.left,res,col-1,row+1)
        self.helper(root.right,res,col+1,row+1)
        

    
        
        
            
        