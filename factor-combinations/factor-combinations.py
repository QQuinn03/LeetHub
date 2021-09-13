class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n ==1:
            return []
        res = []
        path =[]
        self.helper(n,2,res,path)
        return res
    
    def helper(self,n,i,res,path):
        
        while i*i<=n:
            if n%i==0:
                res+=[path+[i,n/i]]
                self.helper(n/i,i,res,path+[i])
            i+=1
        
            