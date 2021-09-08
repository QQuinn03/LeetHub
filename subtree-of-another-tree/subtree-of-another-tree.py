# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False
        s1 = self.helper(s,[])
        t1 = self.helper(t,[])
        for i in t1:
            if i not in s1:
                return False
        # return True    
        new1 = "".join(s1)
        new2 = "".join(t1)
        if new2 in new1:
            return True
        return False
    
    def helper(self,root,path):
        if not root:
            path.append("#")
            return 
        else:
            path.append(str(root.val))
        self.helper(root.left,path)
        self.helper(root.right,path)
        return path
            
            