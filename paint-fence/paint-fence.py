class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n ==1:
            return k
        if n ==2:
            return k*k
        
        res = [0]*(n+1)
        res[1]=k
        res[2]=k*k
        
        for i in range(3,len(res)):
            res[i]=(k-1)*(res[i-1]+res[i-2])
        return res[n]    