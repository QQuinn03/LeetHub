class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=[i]
            else:
                dic[s[i]].append(i)
        ans=float("inf")
        for i,val in dic.items():
            if len(val)==1:
                if val[0]<ans:
                    ans=val[0]
        if ans==float("inf"):
            return -1
        return ans            
                
                