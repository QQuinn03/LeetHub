class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0:
            return 0
        res=[0]*(N+1)
        res[1]=1
        for i in range(2,len(res)):
            res[i]=res[i-1]+res[i-2]
        return res[-1]    