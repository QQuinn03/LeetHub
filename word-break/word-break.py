class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0]=True
        
        for i in range(len(dp)):
            if dp[i]==True:
                for j in range(i+1,len(dp)):
                    if s[i:j] in wordDict:
                        dp[j]=True
        return dp[-1]                