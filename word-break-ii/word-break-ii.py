class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        self.dfs(s,wordDict,res,"")
        return res
    def dfs(self,s,wordDict,res,path):
        if self.check(s,wordDict):
            
            if not s:
                print("h")
                res.append(path[:-1])
                print(res)
                return 
            for i in range(len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:],wordDict,res,path+s[:i]+" ")
            
        
                
    
    def check(self,s,wordDict):
        dp = [0]*(len(s)+1)
        dp[0]=1
        
        for i in range(len(s)):
            if dp[i]==1:
                for j in range(i,len(s)):
                    if s[i:j+1] in wordDict:
                        dp[j+1]=1
                    
        return dp[-1]                
        
    