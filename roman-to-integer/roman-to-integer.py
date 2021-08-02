class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res = 0
        
        while s:
            letter = s[0]
            
            if len(s)==1:
                res+=dic[letter]
                return res
            if dic[letter]>=dic[s[1]]:
                res+=dic[letter]
                s = s[1:]
            elif dic[letter]<dic[s[1]]:
                res +=dic[s[1]]-dic[letter]
                s=s[2:]
        return res        