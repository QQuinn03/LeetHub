class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1=len(word1)
        len2=len(word2)
        
        if len1*len2==0:
            return len1+len2
        dp=[[0 for i in range(len1+1)]for j in range(len2+1)]
        
        for i in range(len(dp)):
            dp[i][0]=i
        for j in range(len(dp[0])):
            dp[0][j]=j
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if word2[i-1]!=word1[j-1]:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]-1)
        return dp[-1][-1]             
            