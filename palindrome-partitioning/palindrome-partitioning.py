class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        self.helper(res,s,[])
        return res
    
    def helper(self,res,s,path):
        if not s:
            res.append(path)
            return 
        for i in range(1,len(s)+1):
            if self.check(s[:i])==True:
                self.helper(res,s[i:],path+[s[:i]])
                
    def check(self,s):
        return s==s[::-1]