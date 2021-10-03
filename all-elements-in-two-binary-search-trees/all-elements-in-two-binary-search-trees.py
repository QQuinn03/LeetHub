# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        arr1=self.inorder(root1,[])
        arr2 = self.inorder(root2,[])
        if not arr1:
            return arr2
        if not arr2:
            return arr1
        idx1=0
        idx2=0
        res=[]
        while idx1<len(arr1) or idx2<len(arr2):
            if idx1==len(arr1):
                res.append(arr2[idx2])
                idx2+=1
            elif idx2 ==len(arr2):
                res.append(arr1[idx1])
                idx1+=1
            else:
                if arr1[idx1]<=arr2[idx2]:
                    res.append(arr1[idx1])
                    idx1+=1
                else:
                    res.append(arr2[idx2])
                    idx2+=1
               
        return res           
    def inorder(self,root,res):
        if not root:
            return 
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
        return res
                
            
            
            