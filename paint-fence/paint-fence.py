class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n ==1:
            return k
        if n==2:
            return k*k
        
        res=[0 for i in range(n)]
        res[0]=k
        res[1]=k*k
        for i in range(2,len(res)):
            res[i]=(k-1)*(res[i-1]+res[i-2])
        return res[-1]    
            
            