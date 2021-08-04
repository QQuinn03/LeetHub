class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""
        self.helper(res,path,n,n)
        return res
    
    def helper(self,res,path,left,right):
        if left<0 or right<0:
            return 
        if left ==0 and right ==0:
            res.append(path)
            return
        if left==right:
            self.helper(res,path+"(",left-1,right)
        elif left<right:
            self.helper(res,path+"(",left-1,right)
            self.helper(res,path+")",left,right-1)
            