class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        if ns>nt:
            return self.isOneEditDistance(t,s)
        
        for i in range(ns):
            if s[i]!=t[i]:
                if ns==nt:
                    return s[i+1:]==t[i+1:]
                else:
                    return s[i:]==t[i+1:]
                   
        return ns+1==nt        