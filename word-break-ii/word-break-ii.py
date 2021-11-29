class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res=[]
        self.dfs(s,wordDict,"",res)
        return res
    def dfs(self,s,wordDict,path,res):
        if self.check(s,wordDict):
            if not s:
                res.append(path[:-1])
                return 
            for i in range(len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:],wordDict,path+s[:i]+" ",res)
       
    def check(self,s,wordDict):
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        
        for i in range(len(dp)):
            if dp[i]==True:
                for j in range(i+1,len(dp)):
                    if s[i:j] in wordDict:
                        dp[j]=True
        return dp[-1]                
        
                    
        