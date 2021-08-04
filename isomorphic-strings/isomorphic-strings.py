class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        
        for i in range(len(s)):
            if s[i] in dic2 and dic2[s[i]]!=t[i]:
                return False
            if t[i] in dic1 and dic1[t[i]]!=s[i]:
                return False
            dic1[t[i]]=s[i]
            dic2[s[i]]=t[i]
        return True    