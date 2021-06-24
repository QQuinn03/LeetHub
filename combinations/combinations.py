class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        self.helper(n,k,res,path,1)
        return res
    
    def helper(self,n,k,res,path,i):
        if len(path)==k:
            res.append(path)
        else:
            
            for i in range(i,n+1):
                
                self.helper(n,k,res,path+[i],i+1)
                
                
