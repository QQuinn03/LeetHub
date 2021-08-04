import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
			# Corner case handle
            return 0
        
        dp = [1]*n
        dp[0]=0
        dp[1]=0
        m = 2
        
        while m*m<n:
            if dp[m]==1:
                for i in range(m*m,n,m):
                    dp[i]=0
            if m ==2:
                m+=1
            else:
                m+=2
        return sum(dp)        
        
        